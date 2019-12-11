import sys
import json
from pprint import pprint

def parseInput():
    if len(sys.argv) > 1:
        return sys.argv
    return ['invalidService']

def invalidService(args):
    return 'Invalid Service'

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

def typesOfWorkoutsPerPerson(args):
    from Core.Activities import Activities
    from Data.RowlogApi import getWorkoutData
    from Service import TypesOfWorkoutsPerPerson
    return TypesOfWorkoutsPerPerson.run(getWorkoutData(orderBy='wid', comment=''), Activities)

def workoutsPerPerson(args):
    from Data.RowlogApi import getWorkoutData
    from Service import WorkoutsPerPerson
    return WorkoutsPerPerson.run(getWorkoutData(orderBy='wid', comment=''))

def totalMetersPerSide(args):
    from Data.RowlogApi import getWorkoutData
    from Data.RowlogApi import getPeopleData
    from Service import TotalMetersPerSide
    return TotalMetersPerSide.run(getWorkoutData(orderBy='wid', comment=''), getPeopleData())

def averageMetersPerSide(args):
    from Data.RowlogApi import getWorkoutData
    from Data.RowlogApi import getPeopleData
    from Service import AverageMetersPerSide
    return AverageMetersPerSide.run(getWorkoutData(orderBy='wid', comment=''), getPeopleData())

def metersAndSplitPerBoat(args):
    from Data.RowlogApi import getWorkoutData
    from Data.RowlogApi import getPeopleData
    from Core import SplitManager
    from Service import MetersAndSplitPerBoat
    return MetersAndSplitPerBoat.run(getWorkoutData(orderBy='wid', comment=''), getPeopleData(), SplitManager)


switcher = {
    'averageMetersPerSide': averageMetersPerSide,
    'ergMetersPerDay': ergMetersPerDay,
    'invalidService': invalidService,
    'individualContributions': individualContributions,
    'metersAndSplitPerBoat': metersAndSplitPerBoat,
    'totalMetersPerSide': totalMetersPerSide,
    'typesOfWorkoutsPerPerson': typesOfWorkoutsPerPerson,
    'workoutsPerPerson': workoutsPerPerson
    
}
 
def serviceSwitch(arguments):
    service = switcher.get(arguments[1], invalidService)
    return service(arguments)

output = serviceSwitch(parseInput())
print(json.dumps(output))
