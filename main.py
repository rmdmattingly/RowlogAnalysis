import sys
import json
from pprint import pprint

def parseInput():
    if len(sys.argv) > 2:
        return sys.argv
    return ['invalidService']

def invalidService(args):
    return 'Invalid Service'

def averageMetersPerSide(args):
    from Data.RowlogApi import getWorkoutData
    from Data.RowlogApi import getPeopleData
    from Service import AverageMetersPerSide
    return AverageMetersPerSide.run(getWorkoutData(teamCode=args[1], orderBy='wid', comment=''), getPeopleData(teamCode=args[1]))

def ergMetersPerDay(args):
    from Core import DateManager
    from Core.Activities import Activities
    from Data.RowlogApi import getWorkoutData
    from Service import ErgMetersPerDay
    return ErgMetersPerDay.run(getWorkoutData(teamCode=args[1], orderBy='time', comment=''), Activities, DateManager)

def individualContributions(args):
    from Core import DateManager
    from Core.Activities import Activities
    from Data.RowlogApi import getPeopleData
    from Data.RowlogApi import getWorkoutData
    from Service import IndividualContributions
    return IndividualContributions.run(getWorkoutData(teamCode=args[1], orderBy='time', comment=''), getPeopleData(teamCode=args[1]), DateManager)

def searchComments(args):
    from Data.RowlogApi import getWorkoutData
    return getWorkoutData(teamCode=args[1], orderBy='wid', comment=args[3])

def typesOfWorkoutsPerPerson(args):
    from Core.Activities import Activities
    from Data.RowlogApi import getWorkoutData
    from Service import TypesOfWorkoutsPerPerson
    return TypesOfWorkoutsPerPerson.run(getWorkoutData(teamCode=args[1], orderBy='wid', comment=''), Activities)

def totalMetersPerSide(args):
    from Data.RowlogApi import getWorkoutData
    from Data.RowlogApi import getPeopleData
    from Service import TotalMetersPerSide
    return TotalMetersPerSide.run(getWorkoutData(teamCode=args[1], orderBy='wid', comment=''), getPeopleData(teamCode=args[1]))

def longestWorkoutPerDay(args):
    from Core import DateManager
    from Data.RowlogApi import getWorkoutData
    from Service import LongestWorkoutPerDay
    return LongestWorkoutPerDay.run(getWorkoutData(teamCode=args[1], orderBy='time', comment=''), DateManager)

def workoutsPerPerson(args):
    from Data.RowlogApi import getWorkoutData
    from Service import WorkoutsPerPerson
    return WorkoutsPerPerson.run(getWorkoutData(teamCode=args[1], orderBy='wid', comment=''))

def totalMetersPerSide(args):
    from Data.RowlogApi import getWorkoutData
    from Data.RowlogApi import getPeopleData
    from Service import TotalMetersPerSide
    return TotalMetersPerSide.run(getWorkoutData(teamCode=args[1], orderBy='wid', comment=''), getPeopleData(teamCode=args[1]))

def percentOfMeters(args):
    from Core.Activities import Activities
    from Data.RowlogApi import getWorkoutData
    from Data.RowlogApi import getPeopleData
    from Service import PercentOfMeters
    return PercentOfMeters.run(getPeopleData(teamCode=args[1]), getWorkoutData(teamCode=args[1], orderBy='wid', comment=''), Activities)

def averageMetersAndSplitBySide(args):
    from Data.RowlogApi import getWorkoutData
    from Data.RowlogApi import getPeopleData
    from Core import SplitManager
    from Service import AverageMetersAndSplitBySide
    return AverageMetersAndSplitBySide.run(getWorkoutData(teamCode=args[1], orderBy='wid', comment=''), getPeopleData(teamCode=args[1]), SplitManager)

switcher = {
    'averageMetersAndSplitBySide': averageMetersAndSplitBySide,
    'averageMetersPerSide': averageMetersPerSide,
    'ergMetersPerDay': ergMetersPerDay,
    'invalidService': invalidService,
    'individualContributions': individualContributions,
    'longestWorkoutPerDay': longestWorkoutPerDay,
    'percentOfMeters': percentOfMeters,
    'searchComments': searchComments,
    'totalMetersPerSide': totalMetersPerSide,
    'typesOfWorkoutsPerPerson': typesOfWorkoutsPerPerson,
    'workoutsPerPerson': workoutsPerPerson
}

def serviceSwitch(arguments):
    service = switcher.get(arguments[2], invalidService)
    return service(arguments)

output = serviceSwitch(parseInput())
print(json.dumps(output))
