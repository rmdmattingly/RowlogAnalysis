def isValidIntensity(intensity):
 return intensity != 'Warmup' and intensity is not None

def isValidActivity(activity):
 return activity == 'Erg'

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
    for name, nameValues in splitTrendData.items():
        averageData[name] = {}
        for date, dateValues in nameValues.items():
            averageData[name][date] = {}
            for intensity, split in dateValues.items():
                calculatedAverage = splitTrendData[name][date][intensity]/workoutCount[name][date][intensity]
                averageData[name][date][intensity] = SplitManager.convertSecondsToSplit(calculatedAverage)
    return averageData

def run(workoutData, SplitManager, DateManager):
    return findSplitTrends(workoutData, SplitManager, DateManager)