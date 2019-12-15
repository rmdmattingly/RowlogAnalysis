def getNameToDataDict(peopleData):
    nameToData = {}
    for ppl in peopleData:
        nameToData[ppl['name']] = ppl
    return nameToData


def getDisplay(workoutsData, Activites, nameToData):
    numOfWork = {}

    for workout in workoutsData:
        type = workout['type']
        name = workout['name']
        if name not in numOfWork:
            numOfWork[name] = {}
            numOfWork[name]['total'] = 0
        numOfWork[name]['total'] += 1
        for activity in Activites:
            if (activity.name not in numOfWork[name].keys()):
                numOfWork[name][activity.name] = {}
                numOfWork[name][activity.name]['NumberOfWorkouts'] = 0
                numOfWork[name][activity.name]['PercentageOfWork'] = 0
            if type in activity.name:
                numOfWork[name][activity.name]['NumberOfWorkouts'] += 1
                numOfWork[name][activity.name]['PercentageOfWork'] = round(100 * float(numOfWork[name][activity.name]['NumberOfWorkouts'])/float(numOfWork[name]['total']), 2)

    return numOfWork

def percentOfMeters(peopleData, getWorkoutData, Activities):
    nameToData = getNameToDataDict(peopleData)
    myDict = {}
    myDict['name'] = getDisplay(getWorkoutData, Activities, nameToData)
    return myDict

def run(peopleData, getWorkoutData, Activities):
    return percentOfMeters(peopleData, getWorkoutData, Activities)
