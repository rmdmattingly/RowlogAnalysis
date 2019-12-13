def findSplitTrendsByPerson(workoutData, people_id, SplitManager, DateManager, intensity):
    orderedWorkoutData = DateManager.getWorkoutsDataChronologically(workoutData)
    workoutsAtIntesnity = {}
    for workout in orderedWorkoutData:
        if workout['people_id'] == people_id and workout['type'] == 'Erg':
            if workout['intensity'] == intensity:
              workoutsAtIntensity[workout['time']] = workout['avg_split']
    return workoutsAtIntensity

def run(workoutData, people_id, SplitManager, DateManager):
    output = {}
    output['U1'] = findSplitTrendByPerson(workoutData, people_id, SplitManager, DateManager, 'U1')
    output['U2'] = findSplitTrendByPerson(workoutData, people_id, SplitManager, DateManager, 'U2')
    output['U3'] = findSplitTrendByPerson(workoutData, people_id, SplitManager, DateManager, 'U3')
    output['AT'] = findSplitTrendByPerson(workoutData, people_id, SplitManager, DateManager, 'AT')
    output['TR'] = findSplitTrendByPerson(workoutData, people_id, SplitManager, DateManager, 'TR')
    output['Test'] = findSplitTrendByPerson(workoutData, people_id, SplitManager, DateManager, 'Test')
    return output

            
            
            
            
