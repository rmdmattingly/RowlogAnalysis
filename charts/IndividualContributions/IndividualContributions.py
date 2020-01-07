import random

def getDaysFromUniversalAvg(data):
    days = []
    for key in data.keys():
        days.append(key)
    return days

def populateDataset(dataset, data, xs, ColorHelper):
    for x in xs:
        if x in data.keys():
            dataset.addData(data[x])
        else:
            dataset.addData(0)
    color = ColorHelper.generateRandomRgbaColor(0.8)
    dataset.addBackgroundColor(color)
    dataset.addBorderColor(color)
    return dataset

def formatData(ChartConfig, ChartOptions, ChartDataset, data, ColorHelper):
    chartOptions = ChartOptions()
    chartConfig = ChartConfig('line', chartOptions)
    xs = getDaysFromUniversalAvg(data["universalAvg_metersPerDay"])
    chartConfig.setXAxesData(xs)
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
        chartConfig.addDataset(populateDataset(dataset, data[key], xs, ColorHelper))
    for person in data['byPerson_metersPerDay']:
        dataset = ChartDataset()
        dataset.setLabel(person)
        chartConfig.addDataset(populateDataset(dataset, data['byPerson_metersPerDay'][person], xs, ColorHelper))
    return chartConfig.toJson()
