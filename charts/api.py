import json
import flask
import requests
from flask import request, jsonify

from Core.ChartConfig import ChartConfig
from Core.ChartOptions import ChartOptions
from Core.ChartData import ChartDataset

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def getService(teamCode, service):
    url = 'https://rows.tech/api/analysis?teamCode=' + str(teamCode) + '&service=' + str(service)
    return json.loads(requests.get(url).text)

@app.route('/', methods=['GET'])
def home():
    return 'Charts api is running!'

@app.route('/individualContributions', methods=['GET'])
def individualContributions():
    from IndividualContributions import IndividualContributions
    from Core import ColorHelper
    teamCode = request.args.get('teamCode')
    service = 'individualContributions'
    data = getService(teamCode, service)
    return IndividualContributions.formatData(ChartConfig, ChartOptions, ChartDataset, data, ColorHelper)

if __name__ == '__main__':
    app.run()
