import requests
from pprint import pprint

### useful functions ###
def sortDictionaryByValues(dictionary):
    return sorted(dictionary.items(), key=lambda kv: kv[1], reverse=True)

def getData(url):
    response = requests.get(url)
    return response.json()

def getWorkoutsPerPerson(workoutsData):
    workoutsPerPerson = {}
    for workout in workoutsData:
        name = workout['name']
        if name not in workoutsPerPerson:
            workoutsPerPerson[name] = 0
        workoutsPerPerson[name] += 1
    return sortDictionaryByValues(workoutsPerPerson)

### Script begins below ###
url = 'https://quikfo.com/rowlog/api/workouts'
workoutsData = getData(url)
workoutsPerPerson = getWorkoutsPerPerson(workoutsData)
pprint(workoutsPerPerson)
