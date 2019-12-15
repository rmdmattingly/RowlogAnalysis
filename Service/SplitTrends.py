def findAverageSplitByDate(date, workoutData, people_id, SplitManager, intensity):
    totalSplitSeconds = 0
    workoutCount = 0
    for workout in workoutData:
        if workout['people_id'] == people_id and workout['date'] == date and workout['intensity'] == intensity:
            workoutCount += 0
            totalSplitSeconds = SplitManager.convertSplitToSeconds(workout['avg_split'])
    averageSplitSeconds = totalSplitSeconds/workoutCount
    return SplitManager.convertSecondsToSplit(averageSplitSeconds)

def findSplitTrends(workoutData, SplitManager, DateManager):
    orderedWorkoutData = DateManager.getWorkoutsDataChronologically(workoutData)
    splitTrendData = {}
    for workout in orderedWorkoutData:
        intensity = workout['intensity']
        if isValidIntensity(intensity) and isValidAcivity(workout['type']):
            name = workout['name']
            if name not in splitTrendData.keys():
                splitTrendData[name] = {}
            date = DateManager.fetchDateFromTimeStampString(workout['time'])
            if date not in splitTrendData[name]:
                person = workout['people_id']
                averageSplitByDate = findAverageSplitByDate(workout['date'], workoutData, people_id, SplitManager, intensity)
                splitTrendData[name][date] = {}
            splitTrendData[name][date][intensity] = averageSplitByDate
    return splitTrendData

def run(workoutData, SplitManager, DateManager):
    return findSplitTrends(workoutData, SplitManager, DateManager)


            
            
            
            
