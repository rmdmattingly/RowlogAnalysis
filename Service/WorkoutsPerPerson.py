import requests

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

def run():
    url = 'https://quikfo.com/rowlog/api/workouts'
    workoutsData = getData(url)
    return getWorkoutsPerPerson(workoutsData)
