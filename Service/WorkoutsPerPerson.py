def sortDictionaryByValues(dictionary):
    return sorted(dictionary.items(), key=lambda kv: kv[1], reverse=True)

def getWorkoutsPerPerson(workoutsData):
    workoutsPerPerson = {}
    for workout in workoutsData:
        name = workout['name']
        if name not in workoutsPerPerson:
            workoutsPerPerson[name] = 0
        workoutsPerPerson[name] += 1
    return sortDictionaryByValues(workoutsPerPerson)

def run(workoutsData):
    return getWorkoutsPerPerson(workoutsData)
