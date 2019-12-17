def isValidIntensity(intensity):
 return intensity != 'Warmup' and intensity is not None

def intensityCountToPercentage(intensityCount, totalWorkoutCount):
    intensityPercentageData = {}
    for name, intensityData in intensityCount.items():
        intensityPercentageData[name] = {}
        for intensity, value in intensityData.items():
            percentAtIntensity = round(100*(value/totalWorkoutCount[name]))
            intensityPercentageData[name][intensity] = percentAtIntensity
    return intensityPercentageData


def findIntensityPercentages(workoutData):
    intensityCount = {}
    totalWorkoutCount = {}
    for workout in workoutData:
        if isValidIntensity(workout['intensity']):
            name = workout['name']
            if name not in intensityCount.keys():
                intensityCount[name] = {}
            if name not in totalWorkoutCount.keys():
                totalWorkoutCount[name] = 0
            intensity = workout['intensity']
            if intensity not in intensityCount[name].keys():
                intensityCount[name][intensity] = 0
                intensityCount[name][intensity] += 1
                totalWorkoutCount[name] +=1
            intensityCount[name][intensity] += 1
            totalWorkoutCount[name] += 1
    return intensityCountToPercentage(intensityCount, totalWorkoutCount)

def run(workoutData):
    return findIntensityPercentages(workoutData)
