import requests
import collections
from collections import defaultdict
from pprint import pprint
import enum

class WorkoutTypes(enum.Enum):
    Erg = 0
    Bike = 1
    Run = 2
    Swim = 3

### useful functions ###
def sortDictionaryByValues(dictionary):
    return sorted(dictionary.items(), key=lambda kv: kv[1], reverse=True)

def getData(url):
    response = requests.get(url)
    return response.json()

def getTypesOfWorkoutsPerPerson(workoutsData):
    typesOfWorkoutsPerPerson = {}
    for workout in workoutsData:
        name = workout['name']
        type = workout['type']
        if name not in typesOfWorkoutsPerPerson:
            typesOfWorkoutsPerPerson[name] = list(range(0,3))
        for activity in WorkoutTypes:
            if activity not in typesOfWorkoutsPerPerson[name]:
                typesOfWorkoutsPerPerson[name][activity.value] = 0
            if type in activity:
                typesOfWorkoutsPerPerson[name][activity.value] += 1

    return sortDictionaryByValues(workoutsPerPerson)

    return sortDictionaryByValues(typesOfWorkoutsPerPerson)



### Script begins below ###
url = 'https://quikfo.com/rowlog/api/workouts'
workoutsData = getData(url)
typesOfWorkoutsPerPerson = getTypesOfWorkoutsPerPerson(workoutsData)
pprint(typesOfWorkoutsPerPerson)
