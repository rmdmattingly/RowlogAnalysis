import json
import requests

def getNames(teamCode):
    url = 'https://rows.tech/api/people?teamCode=' + str(teamCode)
    return list(map(lambda person: person["name"], json.loads(requests.get(url).text)))

def getBoats():
    return ['1v', '2v', '3v', '4v+']

def convertKey(serviceName, paramName):
    return serviceName + "_" + paramName

def instantiateParamOptions(teamCode):
    paramOptions = {}
    paramOptions[convertKey('individualContributions', 'name')] = getNames(teamCode)
    paramOptions[convertKey('workoutIntensityBreakdown', 'name')] = getNames(teamCode)
    paramOptions[convertKey('workoutIntensityBreakdownBoat', 'boat')] = getBoats()
    return paramOptions

def getParameters(teamCode, service, productionReadyChartServices):
    if service == None:
        return {}
    relevantProdService = None
    print(service)
    for prodService in productionReadyChartServices:
        print(prodService.getChartServiceName())
        if prodService.getChartServiceName() == service:
            relevantProdService = prodService
            break
    params = relevantProdService.getParameters()
    recommendedOptions = {}
    serviceName = relevantProdService.getChartServiceName()
    paramOptions = instantiateParamOptions(teamCode)
    for param in params:
        field = param.getField()
        options = paramOptions[convertKey(serviceName, field)]
        recommendedOptions[field] = options
    return recommendedOptions
