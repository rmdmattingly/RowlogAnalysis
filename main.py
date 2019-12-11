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
<<<<<<< HEAD
    return TypesOfWorkoutsPerPerson.run(getWorkoutData(), Activities)

def weeklyLeardboard(args):
    from Data.RowlogApi import getWorkoutData
    from Service import weeklyLeaderboard
    return weeklyLeaderboard.run(getWorkoutData())
    

switcher = {
    'weeklyLeaderboard': weeklyLeaderboard,
    'workoutsPerPerson': workoutsPerPerson,
=======
    return TypesOfWorkoutsPerPerson.run(getWorkoutData(orderBy='wid', comment=''), Activities)

def totalMetersPerSide(args):
    from Data.RowlogApi import getWorkoutData
    from Data.RowlogApi import getPeopleData
    from Service import TotalMetersPerSide
    return TotalMetersPerSide.run(getWorkoutData(orderBy='wid', comment=''), getPeopleData())

def workoutsPerPerson(args):
    from Data.RowlogApi import getWorkoutData
    from Service import WorkoutsPerPerson
    return WorkoutsPerPerson.run(getWorkoutData(orderBy='wid', comment=''))

switcher = {
    'averageMetersPerSide': averageMetersPerSide,
    'ergMetersPerDay': ergMetersPerDay,
    'invalidService': invalidService,
    'individualContributions': individualContributions,
    'searchComments': searchComments,
    'totalMetersPerSide': totalMetersPerSide,
>>>>>>> a0277bd74b4f9d03c0cf6cc4f7ab437bc8abc066
    'typesOfWorkoutsPerPerson': typesOfWorkoutsPerPerson,
    'workoutsPerPerson': workoutsPerPerson
}

def serviceSwitch(arguments):
    service = switcher.get(arguments[1], invalidService)
    return service(arguments)

output = serviceSwitch(parseInput())
print(json.dumps(output))
