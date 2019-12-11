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
    sideTotalMeters = 0
    sideTotalRowers = findNumberOfRowersOnSide(peopleData, side)
    for workout in workoutData:
        currentRowerSide = findRowerSide(peopleData, workout['people_id'])
        if currentRowerSide == side:
            sideTotalMeters += float(workout['scored_meters'])
    return sideTotalMeters/sideTotalRowers

def findSideAverageSplit(workoutData, peopleData, side, SplitManager):
    rowersOnSide = findNumberOfRowersOnSide(peopleData, side)
    totalSplitSeconds = 0
    workoutCount = 0
    for workout in workoutData:
        currentRowerSide = findRowerSide(peopleData, workout['people_id'])
        if currentRowerSide == side and workout['type'] == 'Erg':
            workoutCount += 1
            try:
                totalSplitSeconds += SplitManager.convertToSeconds(workout['avg_split'])
            except ValueError:
                print("Something wrong with split format!")
    averageSplitInSeconds = totalSplitSeconds/workoutCount
    averageSplit = SplitManager.convertSecondsToSplit(averageSplitInSeconds)
    return AverageSplit

def findPortAvgMeters(workoutData, peopleData):
    return findSideAverageMeters(workoutData, peopleData, 'port')

def findStarboardAvgMeters(workoutData, peopleData):
    return findSideAverageMeters(workoutData, peopleData, 'starboard')

def run(workoutData, peopleData, splitManager):
    output = {}
    output['portMeters'] = findPortAvgMeters(workoutData, peopleData)
    output['starboardMeters'] = findStarboardAvgMeters(workoutData, peopleData)
    output['starboardAverageSplit'] = findSideAverageSplit(workoutData, peopleData, 'starboard', SplitManager)
    output['portAverageSplit'] = findSideAverageSplit(workoutData, peopleData, 'port', SplitManager)
    output['starboardCount'] = findNumberOfRowersOnSide(peopleData, 'starboard')
    output['portCount'] = findNumberOfRowersOnSide(peopleData, 'port')
    return output
