def getNameToDataDict(peopleData):
    nameToData = {}
    for ppl in peopleData:
        nameToData[ppl['name']] = ppl
    return nameToData

def numOfWork(workoutsData, Activites, nameToData):
    numOfWork = {}
    test = 0
    for name, person in nameToData.items():
        numOfWork[name] = {}
        for activity in Activites:
            if (activity.name not in numOfWork[name].keys()):
                numOfWork[name][activity.name] = {}
                if (activity.name in numOfWork[name].keys()):
                    numOfWork[name][activity.name]['NumberOfWorkouts'] = test
                    numOfWork[name][activity.name]['PercentageOfWork'] = test
    return numOfWork


def percentOfMeters(peopleData, getWorkoutData, Activities):
    nameToData = getNameToDataDict(peopleData)
    myDict = {}
    myDict['name'] = numOfWork(getWorkoutData, Activities, nameToData)
    return myDict

def run(peopleData, getWorkoutData, Activities):
    return percentOfMeters(peopleData, getWorkoutData, Activities)
