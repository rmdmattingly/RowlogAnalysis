import sys
import json
from pprint import pprint

def parseInput():
    if len(sys.argv) > 1:
        return sys.argv
    return ['invalidService']

def invalidService(args):
    return 'Invalid Service'

def averageMetersPerSide(args):
    from Data.RowlogApi import getWorkoutData
    from Data.RowlogApi import getPeopleData
    from Service import AverageMetersPerSide
    return AverageMetersPerSide.run(getWorkoutData(orderBy='wid', comment=''), getPeopleData())

def ergMetersPerDay(args):
    from Core import DateManager
    from Core.Activities import Activities
    from Data.RowlogApi import getWorkoutData
    from Service import ErgMetersPerDay
    return ErgMetersPerDay.run(getWorkoutData(orderBy='time', comment=''), Activities, DateManager)

def individualContributions(args):
    from Core import DateManager
    from Core.Activities import Activities
    from Data.RowlogApi import getPeopleData
    from Data.RowlogApi import getWorkoutData
    from Service import IndividualContributions
    return IndividualContributions.run(getWorkoutData(orderBy='time', comment=''), getPeopleData(), DateManager)

def searchComments(args):
    from Data.RowlogApi import getWorkoutData
    return getWorkoutData(orderBy='wid', comment=args[2])

def typesOfWorkoutsPerPerson(args):
    from Core.Activities import Activities
    from Data.RowlogApi import getWorkoutData
    from Service import TypesOfWorkoutsPerPerson
    return TypesOfWorkoutsPerPerson.run(getWorkoutData(), Activities)

def totalMetersPerSide(args):
    from Data.RowlogApi import getWorkoutData
    from Data.RowlogApi import getPeopleData
    from Service import TotalMetersPerSide
    return TotalMetersPerSide.run(getWorkoutData(orderBy='wid', comment=''), getPeopleData())

def longestWorkoutPerDay(args):
    from Core import DateManager
    from Data.RowlogApi import getWorkoutData
    from Service import LongestWorkoutPerDay
    return LongestWorkoutPerDay.run(getWorkoutData(orderBy='time', comment=''), DateManager)

def workoutsPerPerson(args):
    from Data.RowlogApi import getWorkoutData
    from Service import WorkoutsPerPerson
    return WorkoutsPerPerson.run(getWorkoutData(orderBy='wid', comment=''))

def totalMetersPerSide(args):
    from Data.RowlogApi import getWorkoutData
    from Data.RowlogApi import getPeopleData
    from Service import TotalMetersPerSide
    return TotalMetersPerSide.run(getWorkoutData(orderBy='wid', comment=''), getPeopleData())


def percentOfMeters(args):
    from Core.Activities import Activities
    from Data.RowlogApi import getWorkoutData
    from Data.RowlogApi import getPeopleData
    from Service.TypesOfWorkoutsPerPerson import getTypesOfWorkoutsPerPerson
    from Service import PercentOfMeters
    return PercentOfMeters.run(getPeopleData(), getWorkoutData(orderBy='wid', comment=''), Activities, getTypesOfWorkoutsPerPerson)

def averageMetersAndSplitBySide(args):
    from Data.RowlogApi import getWorkoutData
    from Data.RowlogApi import getPeopleData
    from Core import SplitManager
    from Service import AverageMetersAndSplitBySide
    return AverageMetersAndSplitBySide.run(getWorkoutData(orderBy='wid', comment=''), getPeopleData(), SplitManager)

switcher = {
    'averageMetersAndSplitBySide': averageMetersAndSplitBySide,
    'averageMetersPerSide': averageMetersPerSide,
    'ergMetersPerDay': ergMetersPerDay,
    'invalidService': invalidService,
    'individualContributions': individualContributions,
    'longestWorkoutPerDay': longestWorkoutPerDay,
    'searchComments': searchComments,
    'totalMetersPerSide': totalMetersPerSide,
    'typesOfWorkoutsPerPerson': typesOfWorkoutsPerPerson,
    'percentOfMeters': percentOfMeters,
}

def serviceSwitch(arguments):
    service = switcher.get(arguments[1], invalidService)
    return service(arguments)

output = serviceSwitch(parseInput())
print(json.dumps(output))
