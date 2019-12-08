
def getNameToDataDict(peopleData):
    nameToData = {}
    for ppl in peopleData:
        nameToData[ppl['name']] = ppl
    return nameToData

def getUniversalAverageMetersPerDay(workoutsData, numberOfPeople, DateManager):
    chronologicalData = DateManager.getWorkoutsDataChronologically(workoutsData)
    ergMetersPerDay = {}
    for workout in chronologicalData:
        workoutDate = DateManager.fetchDateFromTimestampString(workout['time'])
        if (workoutDate not in ergMetersPerDay.keys()):
            ergMetersPerDay[workoutDate] = 0
        ergMetersPerDay[workoutDate] += int(workout['scored_meters'])
    for key in ergMetersPerDay.keys():
        ergMetersPerDay[key] = int(ergMetersPerDay[key] / int(numberOfPeople))
    return ergMetersPerDay

def getMetersPerDayByPerson(workoutsData, nameToData, DateManager):
    chronologicalData = DateManager.getWorkoutsDataChronologically(workoutsData)
    byPersonMetersPerDay = {}
    for name, person in nameToData.items():
        byPersonMetersPerDay[name] = {}
    for workout in chronologicalData:
        name = workout['name']
        workoutDate = DateManager.fetchDateFromTimestampString(workout['time'])
        if (workoutDate not in byPersonMetersPerDay[name].keys()):
            byPersonMetersPerDay[name][workoutDate] = 0
        byPersonMetersPerDay[name][workoutDate] += int(workout['scored_meters'])
    return byPersonMetersPerDay

def individualContributions(workoutsData, peopleData, DateManager):
    nameToData = getNameToDataDict(peopleData)
    output = {}
    output['universalAvg_metersPerDay'] = getUniversalAverageMetersPerDay(workoutsData, len(nameToData.keys()), DateManager)
    output['byPerson_metersPerDay'] = getMetersPerDayByPerson(workoutsData, nameToData, DateManager)
    return output
    
def run(workoutsData, peopleData, DateManager):
    return individualContributions(workoutsData, peopleData, DateManager)
