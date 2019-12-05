import requests
from enum import Enum
from GetData import getData
from pprint import pprint

class WorkoutTypes(Enum):
    Erg = 0
    Bike = 1
    Run = 2
    Swim = 3

def getTypesOfWorkoutsPerPerson(workoutsData):
    typesOfWorkoutsPerPerson = {}
    for workout in workoutsData:
        name = workout['name']
        type = workout['type']
        if name not in typesOfWorkoutsPerPerson:
            typesOfWorkoutsPerPerson[name] = {}
        for activity in WorkoutTypes:
            if activity.name not in typesOfWorkoutsPerPerson[name]:
                typesOfWorkoutsPerPerson[name][activity.name] = 0
            if type in activity.name:
                typesOfWorkoutsPerPerson[name][activity.name] += 1
    return typesOfWorkoutsPerPerson

### Script begins below ###
url = 'https://quikfo.com/rowlog/api/workouts'
workoutsData = getData(url)
typesOfWorkoutsPerPerson = getTypesOfWorkoutsPerPerson(workoutsData)
pprint(typesOfWorkoutsPerPerson)
