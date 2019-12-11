import sys
import json
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

def weeklyLeardboard(args):
    from Data.RowlogApi import getWorkoutData
    from Service import weeklyLeaderboard
    return weeklyLeaderboard.run(getWorkoutData())
    

switcher = {
    'weeklyLeaderboard': weeklyLeaderboard,
    'workoutsPerPerson': workoutsPerPerson,
    'typesOfWorkoutsPerPerson': typesOfWorkoutsPerPerson,
    'invalidService': invalidService
}
 
def serviceSwitch(argument):
    service = switcher.get(argument, invalidService)
    try:
        return service()
    except:
        return 'Error occurred'

output = serviceSwitch(parseInput())
print(json.dumps(output))
