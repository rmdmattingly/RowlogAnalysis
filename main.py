import argparse
import json
import sys
from pprint import pprint

def parseInput():
    from Core.ArgumentParser import createArgumentParser
    parser = createArgumentParser()
    return parser.parse_args()

def invalidService(args):
    return 'Invalid Service'

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

def searchByComment(args):
    from Data.RowlogApi import getWorkoutData
    if args.query is not None:
        return getWorkoutData(teamCode=args.teamCode, orderBy='wid', comment=args.query)
    else:
        return 'Inavlid Service Call'

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

def longestWorkoutPerDay(args):
    from Core import DateManager
    from Data.RowlogApi import getWorkoutData
    from Service import LongestWorkoutPerDay
    return LongestWorkoutPerDay.run(getWorkoutData(teamCode=args.teamCode, orderBy='time', comment=''), DateManager)

def workoutsPerPerson(args):
    from Data.RowlogApi import getWorkoutData
    from Service import WorkoutsPerPerson
    return WorkoutsPerPerson.run(getWorkoutData(teamCode=args.teamCode, orderBy='wid', comment=''))

def totalMetersPerSide(args):
    from Data.RowlogApi import getWorkoutData
    from Data.RowlogApi import getPeopleData
    from Service import TotalMetersPerSide
    return TotalMetersPerSide.run(getWorkoutData(teamCode=args.teamCode, orderBy='wid', comment=''), getPeopleData(teamCode=args.teamCode))

def averageMetersAndSplitBySide(args):
    from Data.RowlogApi import getWorkoutData
    from Data.RowlogApi import getPeopleData
    from Core import SplitManager
    from Service import AverageMetersAndSplitBySide
    return AverageMetersAndSplitBySide.run(getWorkoutData(teamCode=args.teamCode, orderBy='wid', comment=''), getPeopleData(teamCode=args.teamCode), SplitManager)

switcher = {
    'averageMetersAndSplitBySide': averageMetersAndSplitBySide,
    'averageMetersPerSide': averageMetersPerSide,
    'ergMetersPerDay': ergMetersPerDay,
    'invalidService': invalidService,
    'individualContributions': individualContributions,
    'longestWorkoutPerDay': longestWorkoutPerDay,
    'searchByComment': searchByComment,
    'totalMetersPerSide': totalMetersPerSide,
    'typesOfWorkoutsPerPerson': typesOfWorkoutsPerPerson,
    'workoutsPerPerson': workoutsPerPerson
}

def serviceSwitch(arguments):
    service = switcher.get(arguments.service, invalidService)
    return service(arguments)

output = serviceSwitch(parseInput())
print(json.dumps(output))
