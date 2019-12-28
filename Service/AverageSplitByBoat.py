def calculateBoatAverageSplit(workoutData, peopleData, boating, BoatManager, SplitManager):
    peopleInBoat = BoatManager.findRowersInBoat(peopleData, boating)
    totalSplitSeconds = 0
    workoutCount = 0
    for workout in workoutData:
            if workout['people_id'] in peopleInBoat and workout['type'] == 'Erg':
                workoutCount += 1
                try:
                    totalSplitSeconds += SplitManager.convertSplitToSeconds(workout['avg_split'])
                except ValueError:
                    print("Something Wrong With Split Format")
    averageSplitInSeconds = totalSplitSeconds/workoutCount
    return SplitManager.convertSecondsToSplit(averageSplitInSeconds)

def run(workoutData, peopleData, SplitManager, BoatManager):
    boats = BoatManager.getBoats(peopleData)
    output = {}
    for boat in boats:
        output[boat] = calculateBoatAverageSplit(workoutData, peopleData, boat, BoatManager, SplitManager)
    return output
