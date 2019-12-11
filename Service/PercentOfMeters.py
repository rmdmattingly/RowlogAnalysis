def getNameToDataDict(peopleData):
    nameToData = {}
    for ppl in peopleData:
        nameToData[ppl['name']] = ppl
    return nameToData

def numOfWork(workoutsData Activites, nameToData):
    numOfWork = {}
    for name in nameToData.items():
        numOfWork[name] = {}
        
    for activity in Activites:
        if (activity.name not in numOfWork[name].keys()):
            numOfWork[name][activity.name] = {}
    return numOfWork

def precentOfMeters(peopleData, getWorkoutData, Activities):
    nameToData = getNameToDataDict(peopleData)
    myDict = {}
    myDict['name'] = numOfWork(getWorkoutData, Activites, nameToData)
    return myDict

def run(peopleData, getWorkoutData, Activities):
    return percentOfMeters(peopleData, getWorkoutData, Activities)
