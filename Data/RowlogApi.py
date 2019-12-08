import requests

# accepts orderyBy = time, real_meters, scored_meters, or avg_heartrate.  Only returns desc, reverse the response for asc (see: Service.ErgMetersPerDay.py)
def getWorkoutData(orderBy):
    url = 'https://quikfo.com/rowlog/api/workouts?orderBy=' + orderBy
    response = requests.get(url)
    return response.json()

def getPeopleData():
    url = 'https://quikfo.com/rowlog/api/people'
    response = requests.get(url)
    return response.json()
