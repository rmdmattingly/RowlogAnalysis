def calculateBoatAverageMetersPerWeek(workoutData, peopleData, boating, BoatManager, SplitManager):
    peopleInBoat = BoatManager.findRowersInBoat(peopleData, boating)
    totalScoredMeters = 0
    workoutCount = 0
    for workout in workoutData:
        if workout['people_id'] in peopleInBoat:
            workoutCount += 1
            totalScoredMeters += int(workout['scored_meters'])
    return int(totalScoredMeters/workoutCount * 7)

def run(workoutData, peopleData, SplitManager, BoatManager):
    boats = BoatManager.getBoats(peopleData)
    output = {}
    for boat in boats:
        output[boat] = calculateBoatAverageMetersPerWeek(workoutData, peopleData, boat, BoatManager, SplitManager)
    return output
