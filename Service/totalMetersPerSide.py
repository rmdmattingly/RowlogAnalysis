def getSideMeters(workoutData, peopleData, side):
    sideMeters = 0
    for workout in workoutData
        if workout.person.side = side
            sideMeters += workout['scored_meters']
        return sideMeters


def getPortMeters(workoutData, peopleData):
    return getSideMeters(workoutData, peopleData, 'port')


def getStarboardMeters(workoutData, peopleData):
    return getSideMeters(workoutData, peopleData, 'starboard')

