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
    color = ColorHelper.generateRandomRgbaColor(0.0)
    dataset.addBackgroundColor(color)
    color = ColorHelper.generateRandomRgbaColor(1.0)
    dataset.addBorderColor(color)
    dataset.setHidden(isHidden)
    return dataset

def addBoatDatasets(data, xs, ColorHelper, ChartDataset, chartConfig):
    keysToNames = {
        "universalAvg_metersPerDay": "Avg Meters Per Day - Team",
        "1v_metersPerDayPerPerson": "Avg Meters Per Day - 1v",
        "2v_metersPerDayPerPerson": "Avg Meters Per Day - 2v",
        "3v_metersPerDayPerPerson": "Avg Meters Per Day - 3v",
        "4v+_metersPerDayPerPerson": "Avg Meters Per Day - 4v+"
    }
    for key in keysToNames.keys():
        isHidden = True
        if key == "universalAvg_metersPerDay":
            isHidden = False
        dataset = ChartDataset()
        dataset.setLabel(keysToNames[key])
        dataset.setBorderWidth(2.5)
        chartConfig.addDataset(populateDataset(dataset, data[key], xs, ColorHelper, isHidden))
    return chartConfig

def addPersonDatasets(data, xs, ColorHelper, ChartDataset, chartConfig, name):
    for person in data['byPerson_metersPerDay']:
        dataset = ChartDataset()
        dataset.setLabel(person)
        isHidden = True
        dataset.setBorderWidth(2)
        if person == name:
            isHidden = False
            dataset.setBorderWidth(3.5)
        chartConfig.addDataset(populateDataset(dataset, data['byPerson_metersPerDay'][person], xs, ColorHelper, isHidden))
    return chartConfig

def formatData(ChartConfig, ChartOptions, ChartDataset, ColorHelper, data, name):
    chartConfig = ChartConfig('line', ChartOptions())
    xs = getDaysFromUniversalAvg(data["universalAvg_metersPerDay"])
    chartConfig.setXAxisData(xs)
    chartConfig = addBoatDatasets(data, xs, ColorHelper, ChartDataset, chartConfig)
    chartConfig = addPersonDatasets(data, xs, ColorHelper, ChartDataset, chartConfig, name)
    return chartConfig.toJson()
