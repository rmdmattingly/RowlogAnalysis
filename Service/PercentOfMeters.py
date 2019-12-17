def calcPercentOfWork(numOfWork, name, activity):
    num = numOfWork[name][activity.name]['NumberOfWorkouts']
    tot = numOfWork[name]['total']
    #print(num, tot)
    return round((100 * float(num)/float(tot)), 2)

def getDisplay(workoutsData, Activites):
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
            if active not in numOfWork[name].keys():
                numOfWork[name][active] = {}
                numOfWork[name][active]['NumberOfWorkouts'] = 0
                numOfWork[name][active]['PercentageOfWork'] = 0
            if type in active:
                numOfWork[name][active]['NumberOfWorkouts'] += 1
            numOfWork[name][active]['PercentageOfWork'] = calcPercentOfWork(numOfWork, name, activity)
    return numOfWork

def percentOfMeters(getWorkoutData, Activities):
    myDict = {}
    myDict['name'] = getDisplay(getWorkoutData, Activities)
    return myDict

def run(getWorkoutData, Activities):
    return percentOfMeters(getWorkoutData, Activities)
