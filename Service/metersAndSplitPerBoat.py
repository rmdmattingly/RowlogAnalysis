from core import SplitManager

def findRowerSide(peopleData, people_id):
    personSide = ''
    for person in peopleData:
        if person['people_id'] == people_id:
            personSide = person['side']
    return personSide

def findNumRowersInBoat(peopleData, boating):
    rowerCount = 0
    for person in peopleData:
        if person['boating'] == boating:
            rowerCount += 1
    return rowerCount

def findRowersInBoat(peopleData, boating):
    peopleInBoat = set()
    for person in peopleData:
        if person['boating'] == boating and boating not in peopleInBoat:
            peopleInBoat.add(person['people_id']
    return peopleInBoat

def calculateBoatAverageSplit(workoutData, peopleData, boating):
    peopleInBoat = findRowersInBoat(peopleData, boating)
    totalSplitSeconds = 0
    workoutCount = 0
    for workout in workoutData:
            if workout['people_id'] in peopleInBoat:
                if workout['type'] == 'erg':
                    workoutCount += 1
                    totalSplitSeconds += convertSplitToSeconds(workout['split'])
    averageSplitInSeconds = totalSplitSeconds/workoutCount
    averageSplit = convertSecondsToSplit(averageSplitInSeconds)
    return averageSplit


def run(workoutData, peopleData):
    output = {}
    output['1v'] = calculateBoatAverageSplit(workoutData, peopleData, '1v')
    output['2v'] = calculateBoatAverageSplit(workoutData, peopleData, '2v')
    output['3v'] = calculateBoatAverageSplit(workoutData, peopleData, '3v')
    output['4v+'] = calculateBoatAverageSplit(workoutData, peopleData, '4v+')
    return output


                
    
