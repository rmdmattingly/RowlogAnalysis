def isValidIntensity(intensity):
 return intensity != 'Warmup' and intensity is not None

def isValidActivity(activity):
 return activity == 'Erg'

def findAverageSplitByDate(date, workoutData, people_id, SplitManager, intensity):
    totalSplitSeconds = 0
    workoutCount = 0
    for workout in workoutData:
        if workout['people_id'] == people_id and workout['time'] == date and workout['intensity'] == intensity:
            workoutCount += 1
            totalSplitSeconds = SplitManager.convertSplitToSeconds(workout['avg_split'])
    if workoutCount > 0:
        averageSplitSeconds = totalSplitSeconds/workoutCount
        return SplitManager.convertSecondsToSplit(averageSplitSeconds)
    return None

def findSplitTrends(workoutData, SplitManager, DateManager):
    orderedWorkoutData = DateManager.getWorkoutsDataChronologically(workoutData)
    splitTrendData = {}
    workoutCount = {}
    for workout in orderedWorkoutData:
        intensity = workout['intensity']
        if isValidIntensity(intensity) and isValidActivity(workout['type']):
            name = workout['name']
            if name not in splitTrendData.keys():
                splitTrendData[name] = {}
                workoutCount[name] = {}
            date = DateManager.fetchDateFromTimestampString(workout['time'])
            if date not in splitTrendData[name]:
                splitTrendData[name][date] = {}
                splitTrendData[name][date][intensity] = 0
                workoutCount[name][date] = {}
                workoutCount[name][date][intensity] = 0
            if intensity not in splitTrendData[name][date]:
                splitTrendData[name][date][intensity] = 0
                workoutCount[name][date][intensity] = 0
            splitTrendData[name][date][intensity] += SplitManager.convertSplitToSeconds(workout['avg_split'])
            workoutCount[name][date][intensity] += 1
    averageData = {}
    return splitTrendData

def run(workoutData, SplitManager, DateManager):
    return findSplitTrends(workoutData, SplitManager, DateManager)