def getNameToDataDict(peopleData):
    nameToData = {}
    for ppl in peopleData:
        nameToData[ppl['name']] = ppl
    return nameToData

def calcPercentOfWork(numOfWork, name, activity):
    return round(100 * float(numOfWork[name][activity.name]['NumberOfWorkouts'])/float(numOfWork[name]['total']), 2)

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
            active = activity.name
            if (active not in numOfWork[name].keys()):
                numOfWork[name][active] = {}
                numOfWork[name][active]['NumberOfWorkouts'] = 0
                numOfWork[name][active]['PercentageOfWork'] = 0
            if type in active:
                numOfWork[name][active]['NumberOfWorkouts'] += 1
                numOfWork[name][active]['PercentageOfWork'] = calcPercentOfWork(numOfWork, name, activity)
    return numOfWork

def percentOfMeters(peopleData, getWorkoutData, Activities):
    nameToData = getNameToDataDict(peopleData)
    myDict = {}
    myDict['name'] = getDisplay(getWorkoutData, Activities, nameToData)
    return myDict

def run(peopleData, getWorkoutData, Activities):
    return percentOfMeters(peopleData, getWorkoutData, Activities)
