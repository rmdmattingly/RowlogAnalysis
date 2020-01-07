import random

def getDaysFromUniversalAvg(data):
    days = []
    for key in data.keys():
        days.append(key)
    return days

def populateDataset(dataset, data, xs, ColorHelper, isHidden):
    for x in xs:
        if x in data.keys():
            dataset.addData(data[x])
        else:
            dataset.addData(0)
    color = ColorHelper.generateRandomRgbaColor(0.8)
    dataset.addBackgroundColor(color)
    dataset.addBorderColor(color)
    dataset.setHidden(isHidden)
    return dataset

def addBoatDatasets(data, xs, ColorHelper, ChartDataset, chartConfig):
    keys = [
        "universalAvg_metersPerDay",
        "1v_metersPerDayPerPerson",
        "2v_metersPerDayPerPerson",
        "3v_metersPerDayPerPerson",
        "4v+_metersPerDayPerPerson"
    ]
    for key in keys:
        dataset = ChartDataset()
        dataset.setLabel(key)
        chartConfig.addDataset(populateDataset(dataset, data[key], xs, ColorHelper, False))
    return chartConfig

def addPersonDatasets(data, xs, ColorHelper, ChartDataset, chartConfig, name):
    for person in data['byPerson_metersPerDay']:
        dataset = ChartDataset()
        dataset.setLabel(person)
        isHidden = True
        if person == name:
            isHidden = False
        chartConfig.addDataset(populateDataset(dataset, data['byPerson_metersPerDay'][person], xs, ColorHelper, isHidden))
    return chartConfig

def formatData(ChartConfig, ChartOptions, ChartDataset, ColorHelper, data, name):
    chartConfig = ChartConfig('line', ChartOptions())
    xs = getDaysFromUniversalAvg(data["universalAvg_metersPerDay"])
    chartConfig.setXAxisData(xs)
    chartConfig = addBoatDatasets(data, xs, ColorHelper, ChartDataset, chartConfig)
    chartConfig = addPersonDatasets(data, xs, ColorHelper, ChartDataset, chartConfig, name)
    return chartConfig.toJson()
