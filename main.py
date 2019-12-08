import sys
import json
from pprint import pprint

def parseInput():
    if len(sys.argv) > 1:
        return sys.argv[1]
    return 'invalidService'

def invalidService():
    return 'Invalid Service'

def ergMetersPerDay():
    from Core import DateParser
    from Core.Activities import Activities
    from Data.RowlogApi import getWorkoutData
    from Service import ErgMetersPerDay
    return ErgMetersPerDay.run(getWorkoutData(orderBy='time'), Activities, DateParser)

def typesOfWorkoutsPerPerson():
    from Core.Activities import Activities
    from Data.RowlogApi import getWorkoutData
    from Service import TypesOfWorkoutsPerPerson
    return TypesOfWorkoutsPerPerson.run(getWorkoutData(orderBy='wid'), Activities)

def workoutsPerPerson():
    from Data.RowlogApi import getWorkoutData
    from Service import WorkoutsPerPerson
    return WorkoutsPerPerson.run(getWorkoutData(orderBy='wid'))
 
switcher = {
    'invalidService': invalidService,
    'ergMetersPerDay': ergMetersPerDay,
    'typesOfWorkoutsPerPerson': typesOfWorkoutsPerPerson,
    'workoutsPerPerson': workoutsPerPerson
}
 
def serviceSwitch(argument):
    service = switcher.get(argument, invalidService)
    try:
        return service()
    except Exception as e:
        print(e)
        return 'Error occurred'

output = serviceSwitch(parseInput())
print(json.dumps(output))
