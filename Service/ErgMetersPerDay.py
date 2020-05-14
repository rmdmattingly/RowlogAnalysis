def ergMetersPerDay(workoutsData, Activities, DateManager):
    chronologicalData = DateManager.getWorkoutsDataChronologically(workoutsData)
    ergMetersPerDay = {}
    for workout in chronologicalData:
        workoutDate = DateManager.fetchDateFromTimestampString(workout['time'])
        if (workoutDate not in ergMetersPerDay.keys()):
            ergMetersPerDay[workoutDate] = 0
        if (workout['type'] == Activities.Erg.name):
            ergMetersPerDay[workoutDate] += int(workout['scored_meters'])
    return ergMetersPerDay

def ergMetersPerWeek(workoutsData, Activities, DateManager):
    chronologicalData = DateManager.getWorkoutsDataChronologically(workoutsData)
    ergMetersPerWeek = {}
    for workout in chronologicalData:
        workoutDate = DateManager.fetchDateFromTimestampString(workout['time'])
        workoutDateWeek = DateManager.getMondayDateFromDate(workoutDate)
        if (workoutDateWeek not in ergMetersPerWeek.keys()):
            ergMetersPerWeek[workoutDateWeek] = 0
        if (workout['type'] == Activities.Erg.name):
            ergMetersPerWeek[workoutDateWeek] += int(workout['scored_meters'])
    return ergMetersPerWeek

def run(workoutsData, Activities, DateManager):
    return ergMetersPerDay(workoutsData, Activities, DateManager)

def run(workoutsData, Activities, DateManager, isWeek):
    if isWeek:
        return ergMetersPerWeek(workoutsData, Activities, DateManager)
    return ergMetersPerDay(workoutsData, Activities, DateManager)
