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
            peopleInBoat.add(person['people_id'])
    return peopleInBoat

def calculateBoatAverageSplit(workoutData, peopleData, boating, SplitManager):
    peopleInBoat = findRowersInBoat(peopleData, boating)
    totalSplitSeconds = 0
    workoutCount = 0
    for workout in workoutData:
            if workout['people_id'] in peopleInBoat and workout['type'] == 'erg':
                workoutCount += 1
                totalSplitSeconds += SplitManager.convertSplitToSeconds(workout['split'])
    averageSplitInSeconds = totalSplitSeconds/workoutCount
    averageSplit = SplitManager.convertSecondsToSplit(averageSplitInSeconds)
    return averageSplit


def run(workoutData, peopleData, SplitManager):
    output = {}
    output['1v'] = calculateBoatAverageSplit(workoutData, peopleData, '1v', SplitManager)
    output['2v'] = calculateBoatAverageSplit(workoutData, peopleData, '2v', SplitManager)
    output['3v'] = calculateBoatAverageSplit(workoutData, peopleData, '3v', SplitManager)
    output['4v+'] = calculateBoatAverageSplit(workoutData, peopleData, '4v+', SplitManager)
    return output


                
    
