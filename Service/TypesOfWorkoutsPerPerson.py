def getTypesOfWorkoutsPerPerson(workoutsData):
    typesOfWorkoutsPerPerson = {}
    for workout in workoutsData:
        name = workout['name']
        type = workout['type']
        if name not in typesOfWorkoutsPerPerson:
            typesOfWorkoutsPerPerson[name] = {}
        for activity in WorkoutTypes:
            if activity.name not in typesOfWorkoutsPerPerson[name]:
                typesOfWorkoutsPerPerson[name][activity.name] = 0
            if type in activity.name:
                typesOfWorkoutsPerPerson[name][activity.name] += 1
    return typesOfWorkoutsPerPerson

def run(workoutsData):
    return getTypesOfWorkoutsPerPerson(workoutsData)
