def getBoats(peopleData):
    boats = set()
    for person in peopleData:
        if person['boating'] not in boats:
            boats.add(person['boating'])
    return boats

def findRowersInBoat(peopleData, boating):
    peopleInBoat = set()
    for person in peopleData:
        if person['boating'] == boating and boating not in peopleInBoat:
            peopleInBoat.add(person['people_id'])
    return peopleInBoat

def findNumRowersInBoat(peopleData, boating):
    rowerCount = 0
    for person in peopleData:
        if person['boating'] == boating:
            rowerCount += 1
    return rowerCount
