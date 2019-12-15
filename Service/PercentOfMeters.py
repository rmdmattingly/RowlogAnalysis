def getNameToDataDict(peopleData):
    nameToData = {}
    for ppl in peopleData:
        nameToData[ppl['name']] = ppl
    return nameToData


def getDisplay(workoutsData, Activites, nameToData, types):
    numOfWork = {}
    total = 0

    for workout in workoutsData:
        type = workout['type']
        name = workout['name']
        if name not in numOfWork:
            numOfWork[name] = {}
        for activity in Activites:
            if (activity.name not in numOfWork[name].keys()):
                numOfWork[name][activity.name] = {}
                numOfWork[name][activity.name]['NumberOfWorkouts'] = 0
                numOfWork[name][activity.name]['PercentageOfWork'] = 0
            if type in activity.name:
                numOfWork[name][activity.name]['NumberOfWorkouts'] += 1
                numOfWork[name][activity.name]['PercentageOfWork'] = 100 * float(numOfWork[name][activity.name]['NumberOfWorkouts'])#/float()

    return numOfWork

#100 * float(numWork)/float(total)

def percentOfMeters(peopleData, getWorkoutData, Activities, types):
    nameToData = getNameToDataDict(peopleData)
    #per = percent(types)
    myDict = {}
    myDict['name'] = getDisplay(getWorkoutData, Activities, nameToData, types)
    return myDict

def run(peopleData, getWorkoutData, Activities, typesOfWorkoutsPerPerson):
    return percentOfMeters(peopleData, getWorkoutData, Activities, typesOfWorkoutsPerPerson)
