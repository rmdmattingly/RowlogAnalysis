def ergMetersPerDay(workoutsData, Activites, DateParser):
    chronologicalData = reversed(workoutsData)
    ergMetersPerDay = {}
    for workout in chronologicalData:
        workoutDate = DateParser.fetchDateFromTimestampString(workout['time'])
        if (workoutDate not in ergMetersPerDay.keys()):
            ergMetersPerDay[workoutDate] = 0
        if (workout['type'] == Activites.Erg.name):
            ergMetersPerDay[workoutDate] += int(workout['scored_meters'])
    return ergMetersPerDay

def run(workoutsData, Activites, DateParser):
    return ergMetersPerDay(workoutsData, Activites, DateParser)
