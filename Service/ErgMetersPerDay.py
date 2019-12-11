def ergMetersPerDay(workoutsData, Activites, DateManager):
    chronologicalData = DateManager.getWorkoutsDataChronologically(workoutsData)
    ergMetersPerDay = {}
    for workout in chronologicalData:
        workoutDate = DateManager.fetchDateFromTimestampString(workout['time'])
        if (workoutDate not in ergMetersPerDay.keys()):
            ergMetersPerDay[workoutDate] = 0
        if (workout['type'] == Activites.Erg.name):
            ergMetersPerDay[workoutDate] += int(workout['scored_meters'])
    return ergMetersPerDay

def run(workoutsData, Activites, DateManager):
    return ergMetersPerDay(workoutsData, Activites, DateManager)
