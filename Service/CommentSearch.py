def getCommentSearch(workoutsData, searchTerm):
    foundWorkouts = {}
    for workout in workoutsData:
        name = workout['name']
        comment = workout['comment']
        if searchTerm in comment:
            foundWorkouts['workout_id'] = workout
    return foundWorkouts

def run(workoutsData, comment):
    return getCommentSearch(workoutsData, searchTerm)
