import requests

def getWorkoutData():
    url = 'https://quikfo.com/rowlog/api/workouts'
    response = requests.get(url)
    return response.json()
