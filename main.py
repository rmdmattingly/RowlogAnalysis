import sys
from pprint import pprint

def parseInput():
    if len(sys.argv) > 1:
        return sys.argv[1]
    return 'invalidService'

def invalidService():
    return 'Invalid Service'

def workoutsPerPerson():
    from Service import WorkoutsPerPerson
    from Data.RowlogApi import getWorkoutData
    return WorkoutsPerPerson.run(getWorkoutData())

def typesOfWorkoutsPerPerson():
    from Core.Activities import Activities
    from Data.RowlogApi import getWorkoutData
    from Service import TypesOfWorkoutsPerPerson
    return TypesOfWorkoutsPerPerson.run(getWorkoutData(), Activities)
 
switcher = {
    'workoutsPerPerson': workoutsPerPerson,
    'typesOfWorkoutsPerPerson': typesOfWorkoutsPerPerson,
    'invalidService': invalidService
}
 
def serviceSwitch(argument):
    service = switcher.get(argument, invalidService)
    return service()

pprint(serviceSwitch(parseInput()))
