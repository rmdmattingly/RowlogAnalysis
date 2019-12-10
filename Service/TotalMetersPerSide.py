def findRowersOnSide(workoutData, peopleData, side):
    listOfIDs = []
    for person in peopleData:
        if person['side'] == side:
            listOfIDs += person['people_id']
    return listOfIDs
    
def getSideMeters(workoutData, peopleData, side):
    sideMeters = 0
    rowersOnSide = findRowersOnSide(workoutData, peopleData, side)
    for workout in workoutData:
        if workout['people_id'] in rowersOnSide:
            sideMeters += workout['scored_meters']
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
