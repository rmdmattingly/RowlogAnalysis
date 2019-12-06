import requests

def getWorkoutData():
    url = 'https://quikfo.com/rowlog/api/workouts'
    response = requests.get(url)
    return response.json()

def getPeopleData():
    url = 'https://quikfo.com/rowlog/api/people'
    response = requests.get(url)
    return response.json()
