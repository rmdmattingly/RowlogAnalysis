import argparse
import json
import sys
from pprint import pprint

def parseInput():
    from Core.ArgumentParser import createArgumentParser
    parser = createArgumentParser()
    return parser.parse_args()

def runBasicTest(args, switcher):
    output = {}
    output["Errors"] = {}
    serviceNum = len(switcher.keys())
    i = 0
    for service in switcher.keys():
        try:
            if service != "basicTest":
                switcher[service](args)
        except Exception as e:
            output["Errors"][service] = "ERROR: " + str(e)
        i += 1
        print("Progress:", round(i / serviceNum, 2))
    return output

def invalidService(args):
    return 'Invalid Service'

def averageMetersAndSplitBySide(args):
    from Data.RowlogApi import getWorkoutData
    from Data.RowlogApi import getPeopleData
    from Core import SplitManager
    from Service import AverageMetersAndSplitBySide
    return AverageMetersAndSplitBySide.run(getWorkoutData(teamCode=args.teamCode, orderBy='wid', comment=''), getPeopleData(teamCode=args.teamCode), SplitManager)

def averageMetersPerWeekByBoat(args):
    from Data.RowlogApi import getWorkoutData
    from Data.RowlogApi import getPeopleData
    from Core import BoatManager
    from Core import SplitManager
    from Service import AverageMetersPerWeekByBoat
    return AverageMetersPerWeekByBoat.run(getWorkoutData(teamCode=args.teamCode, orderBy='wid', comment=''), getPeopleData(teamCode=args.teamCode), SplitManager, BoatManager)

def averageSplitByBoat(args):
    from Data.RowlogApi import getWorkoutData
    from Data.RowlogApi import getPeopleData
    from Core import BoatManager
    from Core import SplitManager
    from Service import AverageSplitByBoat
    return AverageSplitByBoat.run(getWorkoutData(teamCode=args.teamCode, orderBy='wid', comment=''), getPeopleData(teamCode=args.teamCode), SplitManager, BoatManager)

def averageMetersPerSide(args):
    from Data.RowlogApi import getWorkoutData
    from Data.RowlogApi import getPeopleData
    from Service import AverageMetersPerSide
    return AverageMetersPerSide.run(getWorkoutData(teamCode=args.teamCode, orderBy='wid', comment=''), getPeopleData(teamCode=args.teamCode))

def ergMetersPerDay(args):
    from Core import DateManager
    from Core.Activities import Activities
    from Data.RowlogApi import getWorkoutData
    from Service import ErgMetersPerDay
    return ErgMetersPerDay.run(getWorkoutData(teamCode=args.teamCode, orderBy='time', comment=''), Activities, DateManager)

def individualContributions(args):
    from Core import DateManager
    from Core.Activities import Activities
    from Data.RowlogApi import getPeopleData
    from Data.RowlogApi import getWorkoutData
    from Service import IndividualContributions
    return IndividualContributions.run(getWorkoutData(teamCode=args.teamCode, orderBy='time', comment=''), getPeopleData(teamCode=args.teamCode), DateManager)

def intensityPercentages(args):
    from Data.RowlogApi import getWorkoutData
    from Service import IntensityPercentages
    return IntensityPercentages.run(getWorkoutData(teamCode=args.teamCode, orderBy='wid', comment=''))

def longestWorkoutPerDay(args):
    from Core import DateManager
    from Data.RowlogApi import getWorkoutData
    from Service import LongestWorkoutPerDay
    return LongestWorkoutPerDay.run(getWorkoutData(teamCode=args.teamCode, orderBy='time', comment=''), DateManager)

def percentOfMeters(args):
    from Core.Activities import Activities
    from Data.RowlogApi import getWorkoutData
    from Service import PercentOfMeters
    return PercentOfMeters.run(getWorkoutData(teamCode=args.teamCode, orderBy='wid', comment=''), Activities)

def searchByComment(args):
    from Data.RowlogApi import getWorkoutData
    if args.query is not None:
        return getWorkoutData(teamCode=args.teamCode, orderBy='wid', comment=args.query)
    else:
        return 'Inavlid Service Call'

def splitTrends(args):
    from Core import DateManager
    from Core import SplitManager
    from Data.RowlogApi import getWorkoutData
    from Service import SplitTrends
    return SplitTrends.run(getWorkoutData(teamCode=args.teamCode, orderBy='wid', comment=''), SplitManager, DateManager)

def typesOfWorkoutsPerPerson(args):
    from Core.Activities import Activities
    from Data.RowlogApi import getWorkoutData
    from Service import TypesOfWorkoutsPerPerson
    return TypesOfWorkoutsPerPerson.run(getWorkoutData(teamCode=args.teamCode, orderBy='wid', comment=''), Activities)

def totalMetersPerSide(args):
    from Data.RowlogApi import getWorkoutData
    from Data.RowlogApi import getPeopleData
    from Service import TotalMetersPerSide
    return TotalMetersPerSide.run(getWorkoutData(teamCode=args.teamCode, orderBy='wid', comment=''), getPeopleData(teamCode=args.teamCode))

def workoutsPerPerson(args):
    from Data.RowlogApi import getWorkoutData
    from Service import WorkoutsPerPerson
    return WorkoutsPerPerson.run(getWorkoutData(teamCode=args.teamCode, orderBy='wid', comment=''))

switcher = {
    ## test keys ##
    'basicTest': runBasicTest,

    ## service keys ##
    'averageMetersAndSplitBySide': averageMetersAndSplitBySide,
    'averageMetersPerSide': averageMetersPerSide,
    'averageMetersPerWeekByBoat': averageMetersPerWeekByBoat,
    'averageSplitByBoat': averageSplitByBoat,
    'ergMetersPerDay': ergMetersPerDay,
    'invalidService': invalidService,
    'individualContributions': individualContributions,
    'intensityPercentages': intensityPercentages,
    'longestWorkoutPerDay': longestWorkoutPerDay,
    'percentOfMeters': percentOfMeters,
    'searchByComment': searchByComment,
    'splitTrends': splitTrends,
    'totalMetersPerSide': totalMetersPerSide,
    'typesOfWorkoutsPerPerson': typesOfWorkoutsPerPerson,
    'workoutsPerPerson': workoutsPerPerson
}

def serviceSwitch(arguments):
    service = switcher.get(arguments.service, invalidService)
    if arguments.service == "basicTest":
        return service(arguments, switcher)
    return service(arguments)

output = serviceSwitch(parseInput())
print(json.dumps(output))
