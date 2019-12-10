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
    return ErgMetersPerDay.run(getWorkoutData(orderBy='time'), Activities, DateManager)

def IndividualContributions(args):
    from Core import DateManager
    from Core.Activities import Activities
    from Data.RowlogApi import getPeopleData
    from Data.RowlogApi import getWorkoutData
    from Service import IndividualContributions
    return IndividualContributions.run(getWorkoutData(orderBy='time'), getPeopleData(), DateManager)

def typesOfWorkoutsPerPerson(args):
    from Core.Activities import Activities
    from Data.RowlogApi import getWorkoutData
    from Service import TypesOfWorkoutsPerPerson
    return TypesOfWorkoutsPerPerson.run(getWorkoutData(orderBy='wid', comment=''), Activities)

def workoutsPerPerson(args):
    from Data.RowlogApi import getWorkoutData
    from Service import WorkoutsPerPerson
    return WorkoutsPerPerson.run(getWorkoutData(orderBy='wid', comment=''))

def getStarboardMeters():
    from Data.RowLogApi import getWorkoutData
    from Data.RowLogApi import getPeopleData
    from Service import TotalMetersPerSide
    return getSideMeters.getStarboardMeters(getWorkoutData, getPeopleData, 'starboard')

def getPortMeters():
    from Data.RowLogApi import getWorkoutData
    from Data.RowLogApi import getPeopleData
    from Service import TotalMetersPerSide
    return getSideMeters.getPortMeters(getWorkoutData, getPeopleData, 'port')
 
switcher = {
    'ergMetersPerDay': ergMetersPerDay,
    'invalidService': invalidService,
    'individualContributions': IndividualContributions,
    'typesOfWorkoutsPerPerson': typesOfWorkoutsPerPerson,
    'workoutsPerPerson': workoutsPerPerson
}
 
def serviceSwitch(arguments):
    service = switcher.get(arguments[1], invalidService)
    return service(arguments)

output = serviceSwitch(parseInput())
print(json.dumps(output))
