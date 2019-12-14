import requests

# accepts orderyBy = time, real_meters, scored_meters, or avg_heartrate.  Only returns desc, reverse the response for asc (see: Service.ErgMetersPerDay.py)
def getWorkoutData(teamCode, orderBy, comment):
    url = 'https://quikfo.com/rowlog/api/workouts?teamCode=' + teamCode + 'orderBy=' + orderBy + '&comment=' + comment
    response = requests.get(url)
    return response.json()

def getPeopleData(teamCode):
    url = 'https://quikfo.com/rowlog/api/people?teamCode=' + teamCode
    response = requests.get(url)
    return response.json()
