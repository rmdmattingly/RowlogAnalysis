def getLongestWorkoutPerDay(workoutsData, Activites, DateManager):
    longestWorkoutPerDay = {}
    chronologicalData = DateManager.getWorkoutsDataChronologically(workoutsData)
    for workout in chronologicalData:
        workoutDate = DateManager.fetchDateFromTimestampString(workout['time'])
        if workoutDate not in longestWorkoutPerDay.keys():
            longestWorkoutPerDay[workoutDate] = int(workout['scored_meters'])
        elif int(workout['scored_meters']) > longestWorkoutPerDay[workoutDate]:
            longestWorkoutPerDay[workoutDate] = int(workout['scored_meters'])
    return longestWorkoutPerDay


def run(workoutsData, Activites, DateManager):
    return getLongestWorkoutPerDay(workoutsData, Activites, DateManager)
