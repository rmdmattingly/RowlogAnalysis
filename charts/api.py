import json
import flask
import requests
from flask import request, jsonify

from Core.ChartConfig import ChartConfig
from Core.ChartOptions import ChartOptions
from Core.ChartData import ChartDataset
from Core.ChartService import ChartService

app = flask.Flask(__name__)
app.config["DEBUG"] = True

productionReadyChartServices = [
    ChartService('individualContributions', 'individualContributions', 'Individual Contributions')
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

@app.route('/individualContributions', methods=['GET'])
def individualContributions():
    from IndividualContributions import IndividualContributions
    from Core import ColorHelper
    teamCode = request.args.get('teamCode')
    name = request.args.get('name')
    data = getService(teamCode, 'individualContributions')
    return IndividualContributions.formatData(ChartConfig, ChartOptions, ChartDataset, ColorHelper, data, name)

if __name__ == '__main__':
    app.run()
