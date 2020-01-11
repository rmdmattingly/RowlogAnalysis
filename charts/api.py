import json
import flask
import requests
from flask import request, jsonify

from Core.ChartConfig import ChartConfig
from Core.ChartOptions import ChartOptions
from Core.ChartData import ChartDataset
from Core.ChartService import ChartService
from Core.ChartServiceParams import ChartServiceParams

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# when adding a new production ready chart, be sure to add supporting functionality for all recommended parameter options!
##
## NOTES: add workoutIntensityBreakdown recommended params then add to prod ready services
##
productionReadyChartServices = [
    ChartService('individualContributions', 'individualContributions', 'Individual Contributions', [
        ChartServiceParams("name", False)
    ]),
    ChartService('workoutIntensityBreakdown', 'intensityPercentages', 'Workout Intensity Breakdown - Individual', [
        ChartServiceParams("name", True)
    ]),
    ChartService('workoutIntensityBreakdownBoat', 'intensityPercentages', 'Workout Intensity Breakdown - Boat', [
        ChartServiceParams("boat", True)
    ]),
    ChartService('workoutIntensityBreakdownTeam', 'intensityPercentages', 'Workout Intensity Breakdown - Team', [])
]

def getService(teamCode, service):
    url = 'https://rows.tech/api/analysis?teamCode=' + str(teamCode) + '&service=' + str(service)
    return json.loads(requests.get(url).text)

@app.route('/', methods=['GET'])
def home():
    output = {}
    for service in productionReadyChartServices:
        chartServiceName = service.getChartServiceName()
        output[chartServiceName] = service.toJson()
    return output

@app.route('/recommendedParameterOptions', methods=['GET'])
def recommendedParameterOptions():
    from RecommendedParameters import RecommendedParameters
    teamCode = request.args.get('teamCode')
    service = request.args.get('service')
    return RecommendedParameters.getParameters(teamCode, service, productionReadyChartServices)

@app.route('/individualContributions', methods=['GET'])
def individualContributions():
    from IndividualContributions import IndividualContributions
    from Core import ColorHelper
    teamCode = request.args.get('teamCode')
    name = request.args.get('name')
    data = getService(teamCode, 'individualContributions')
    return IndividualContributions.formatData(ChartConfig, ChartOptions, ChartDataset, ColorHelper, data, name)

@app.route('/workoutIntensityBreakdown', methods=['GET'])
def workoutIntensityBreakdown():
    from WorkoutIntensityBreakdown import WorkoutIntensityBreakdown
    from Core import ColorHelper
    teamCode = request.args.get('teamCode')
    name = request.args.get('name')
    data = getService(teamCode, 'intensityPercentages')
    return WorkoutIntensityBreakdown.formatData(ChartConfig, ChartOptions, ChartDataset, data, name)

@app.route('/workoutIntensityBreakdownBoat', methods=['GET'])
def workoutIntensityBreakdownBoat():
    from WorkoutIntensityBreakdown import WorkoutIntensityBreakdown
    from Core import ColorHelper
    from Core.PeopleManager import PeopleManager
    teamCode = request.args.get('teamCode')
    data = getService(teamCode, 'intensityPercentages')
    boat = request.args.get('boat')
    return WorkoutIntensityBreakdown.formatDataBoat(ChartConfig, ChartOptions, ChartDataset, PeopleManager(teamCode), data, boat)

@app.route('/workoutIntensityBreakdownTeam', methods=['GET'])
def workoutIntensityBreakdownTeam():
    from WorkoutIntensityBreakdown import WorkoutIntensityBreakdown
    from Core import ColorHelper
    teamCode = request.args.get('teamCode')
    data = getService(teamCode, 'intensityPercentages')
    return WorkoutIntensityBreakdown.formatDataTeam(ChartConfig, ChartOptions, ChartDataset, data)

if __name__ == '__main__':
    app.run()
