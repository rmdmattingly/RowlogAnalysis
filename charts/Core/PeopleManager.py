class PeopleManager:
    def __init__(self, teamCode):
        self.teamCode = str(teamCode)

    def getPeople(self):
        import json 
        import requests
        url = 'https://rows.tech/api/people?teamCode=' + self.teamCode
        return json.loads(requests.get(url).text)

    def getPeopleToBoatDict(self, people):
        output = {}
        for person in people:
            output[person['name']] = person['boating']
        return output
