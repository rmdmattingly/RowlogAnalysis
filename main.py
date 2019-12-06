import sys
from pprint import pprint

def parseInput():
    if len(sys.argv) > 1:
        return sys.argv[1]
    return 'invalidService'

def invalidService():
    return 'Invalid Service'

def workoutsPerPerson():
    from Data import RowlogApi
    from Service import WorkoutsPerPerson
    return WorkoutsPerPerson.run(RowlogApi.getWorkoutData())

def typesOfWorkoutsPerPerson():
    from Data import RowlogApi
    from Core import WorkoutTypes
    from Service import TypesOfWorkoutsPerPerson
    return TypesOfWorkoutsPerPerson.run(RowlogApi.getWorkoutData())
 
switcher = {
    'workoutsPerPerson': workoutsPerPerson,
    'typesOfWorkoutsPerPerson': typesOfWorkoutsPerPerson,
    'invalidService': invalidService
}
 
def serviceSwitch(argument):
    service = switcher.get(argument, invalidService)
    return service()

pprint(serviceSwitch(parseInput()))
