def findRowersOnSide(workoutData, peopleData, side):
    peopleIDsOnASide = set()
    for person in peopleData:
        if person['side'] == side and side not in peopleIDsOnASide:
            peopleIDsOnASide.add(person['people_id'])
    return peopleIDsOnASide

def getSideMeters(workoutData, peopleData, side):
    sideMeters = 0
    rowersOnSide = findRowersOnSide(workoutData, peopleData, side)
    for workout in workoutData:
        if workout['people_id'] in rowersOnSide:
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
