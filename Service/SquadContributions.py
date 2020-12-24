def calculatePercentages(myData, squad):
    totalMeters = int(squad['squad_meters'])
    for member in squad['members']:
        memberMeters = int(member['person_meters'])
        myData[squad['name']][member['name']] = ( memberMeters / totalMeters)
    return myData

def SquadContributions(squadData):
    myData = {}
    for squad in squadData:
        if squad['name'] not in myData.keys():
            myData[squad['name']] = {}
            myData = calculatePercentages(myData, squad)
    return myData

def run(squadData):
    return SquadContributions(squadData)



