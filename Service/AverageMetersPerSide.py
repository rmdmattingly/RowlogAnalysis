def findNumberOfRowersOnSide(peopleData, side):
    rowerCount = 0
    for person in peopleData:
        if person['side'] == side:
            rowerCount += 1
    return rowerCount

def findRowerSide(peopleData, people_id):
    personSide = ''
    for person in peopleData:
        if person['people_id'] == people_id:
            personSide = person['side']
    return personSide

def findSideAverageMeters(workoutData, peopleData, side):
    sideAverageMeters = 0
    sideTotalMeters = 0
    sideTotalRowers = findNumberOfRowersOnSide(peopleData, side)
    for workout in workoutData:
        currentRowerSide = findRowerSide(peopleData, workout['people_id'])
        if currentRowerSide == side:
            sideTotalMeters += float(workout['scored_meters'])
    sideAverageMeters = sideTotalMeters/sideTotalRowers
    return sideAverageMeters

def findPortAvgMeters(workoutData, peopleData):
    return findSideAverageMeters(workoutData, peopleData, 'port')

def findStarboardAvgMeters(workoutData, peopleData):
    return findSideAverageMeters(workoutData, peopleData, 'starboard')

def run(workoutData, peopleData):
    output = {}
    output['port'] = findPortAvgMeters(workoutData, peopleData)
    output['starboard'] = findStarboardAvgMeters(workoutData, peopleData)
    output['starboardCount'] = findNumberOfRowersOnSide(peopleData, 'starboard')
    output['portCount'] = findNumberOfRowersOnSide(peopleData, 'port')
    return output


    
            
        
