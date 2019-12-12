def findSplitTrendsByPerson(workoutData, people_id, SplitManager, DateManager):
    orderedWorkoutData = DateManager.getWorkoutsDataChronologically(workoutData)
    splitTrendData = {}
    u1Data = {}
    u2Data = {}
    u3Data = {}
    ATData = {}
    TRData = {}
    testData = {}
    for workout in orderedWorkoutData:
        if workout['people_id'] == people_id and workout['type'] == 'Erg':
            workoutDate = DateManager.fetchDateFromTimestampString(workout['time'])
            if workout['intensity'] == 'U1':
                u1Data[workoutDate] = workout['avg_split']
            elif workout['intensity'] == 'U2':
                u2Data[workoutDate] = workout['avg_split']
            elif workout['intensity'] == 'U3':
                u3Data[workoutDate] = workout['avg_split']
            elif workout['intensity'] == 'AT':
                ATData[workoutDate] = workout['avg_split']
            elif workout['intensity'] == 'TR':
                TRData[workoutDate] = workout['avg_split']
            elif workout['intensity'] == 'Test':
                testData[workoutDate] = workout['avg_split']
            elif workout['intensity'] is None:
                pass
            else:
                print("Something went wrong.")
    splitTrendData['U1'] = u1Data
    splitTrendData['U2'] = u2Data
    splitTrendData['U3'] = u3Data
    splitTrendData['AT'] = ATData
    splitTrendData['TR'] = TRData
    splitTrendData['Test'] = testData
    return splitTrendData

def run(workoutData, people_id, SplitManager, DateManager):
    return findSplitTrendsByPerson(workoutData, people_id, SplitManager, DateManager)

            
            
            
            
