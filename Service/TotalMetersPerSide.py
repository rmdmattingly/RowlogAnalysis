def findPersonSide(peopleData, people_id):
    for person in peopleData:
        if person['people_id'] == people_id:
            side = person['side']
    return side
    
def getSideMeters(workoutData, peopleData, side):
    sideMeters = 0
    for workout in workoutData:
        personSide = findPersonSide(peopleData, workout['people_id'])
        if personSide == side:
            sideMeters += float(workout['scored_meters'])
    return sideMeters

def getPortMeters(workoutData, peopleData):
    return getSideMeters(workoutData, peopleData, 'port')

def getStarboardMeters(workoutData, peopleData):
    return getSideMeters(workoutData, peopleData, 'starboard')

def run(workoutData, peopleData):
    output = {}
    output['port'] = getPortMeters(workoutData, peopleData)
    output['starboard'] = getStarboardMeters(workoutData, peopleData)
    return output
