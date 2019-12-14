def getNameToDataDict(peopleData):
    nameToData = {}
    for ppl in peopleData:
        nameToData[ppl['name']] = ppl
    return nameToData


def getDisplay(workoutsData, Activites, nameToData, types):
    numOfWork = {}

    for workout in workoutsData:
        type = workout['type']


    for name, person in nameToData.items():
        numOfWork[name] = {}
        for activity in Activites:
            if (activity.name not in numOfWork[name].keys()):
                numOfWork[name][activity.name] = {}
                if (activity.name in numOfWork[name].keys()):
                        numOfWork[name][activity.name]['NumberOfWorkouts'] += 1
                        numOfWork[name][activity.name]['PercentageOfWork'] = 0

    return numOfWork

#def percent(types):#numWork):
#    for meters in types:
#        total = meters['total_scored_meters']
#        if(total == 0):
#            return 0
##            return total #100 * float(numWork)/float(total)

def percentOfMeters(peopleData, getWorkoutData, Activities, types):
    nameToData = getNameToDataDict(peopleData)
    #per = percent(types)
    myDict = {}
    myDict['name'] = getDisplay(getWorkoutData, Activities, nameToData, types)
    return myDict

def run(peopleData, getWorkoutData, Activities, typesOfWorkoutsPerPerson):
    return percentOfMeters(peopleData, getWorkoutData, Activities, typesOfWorkoutsPerPerson)
