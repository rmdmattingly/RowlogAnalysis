import datetime

def getIntensityDatasets(ChartDataset):
    return {
        'U3': ChartDataset(), 
        'U2': ChartDataset(), 
        'U1': ChartDataset(), 
        'AT': ChartDataset(), 
        'TR': ChartDataset(), 
        'Test': ChartDataset()
    }

def getFreshLastIntensityData():
    return {
        'U3': 'Number.NaN',
        'U2': 'Number.NaN',
        'U1': 'Number.NaN',
        'AT': 'Number.NaN',
        'TR': 'Number.NaN',
        'Test': 'Number.NaN'
    }

def getIntensities():
    return ['U3', 'U2', 'U1', 'AT', 'TR', 'Test']

def getEarliestDay(data):
    earliestDayDate = datetime.datetime.now()
    for person in data.keys():
        for dayStr in data[person].keys():
            dayDate = datetime.datetime.strptime(dayStr, '%Y-%m-%d')
            if dayDate < earliestDayDate:
                earliestDayDate = dayDate
    return earliestDayDate

def getLatestDay(data):
    latestDayDate = datetime.datetime.now() - datetime.timedelta(days=3650)
    for person in data.keys():
        for dayStr in data[person].keys():
            dayDate = datetime.datetime.strptime(dayStr, '%Y-%m-%d')
            if dayDate > latestDayDate:
                latestDayDate = dayDate
    return latestDayDate
    
def getDaysBetweenAndIncluding(earliestDay, latestDay):
    days = []
    movingDay = earliestDay
    while movingDay <= latestDay + datetime.timedelta(days=1):
        days.append(datetime.datetime.strftime(movingDay, '%Y-%m-%d'))
        movingDay += datetime.timedelta(days=1)
    return days

def getAllRelevantDays(data):
    earliestDay = getEarliestDay(data)
    latestDay = getLatestDay(data)
    return getDaysBetweenAndIncluding(earliestDay, latestDay)

def addPersonDatasets(data, xs, ColorHelper, ChartDataset, SplitManager, chartConfig, name):
    intensityDatasets = getIntensityDatasets(ChartDataset)
    lastIntensityData = getFreshLastIntensityData()
    intensities = getIntensities()
    for day in xs:
        if day in data.keys():
            for intensity in intensities:
                if intensity in data[day].keys():
                    lastIntensityData[intensity] = 'null'
                    watts = SplitManager.convertToWatts(data[day][intensity])
                    intensityDatasets[intensity].addData(watts)
                else:
                    intensityDatasets[intensity].addData(lastIntensityData[intensity])
        else:
            for intensity in intensityDatasets.keys():
                intensityDatasets[intensity].addData(lastIntensityData[intensity])
    for intensity in intensityDatasets.keys():
        intensityDatasets[intensity].addBackgroundColor(ColorHelper.getIntensityColor(intensity, 1.0))
        intensityDatasets[intensity].addBorderColor(ColorHelper.getIntensityColor(intensity, 1.0))
        intensityDatasets[intensity].setPointBorderColor(ColorHelper.getIntensityColor(intensity, 1.0))
        intensityDatasets[intensity].setPointBackgroundColor(ColorHelper.getIntensityColor(intensity, 1.0))
        intensityDatasets[intensity].setFill(False)
        intensityDatasets[intensity].setLabel(name + " - " + intensity)
        intensityDatasets[intensity].setBorderWidth(3)
        chartConfig.addDataset(intensityDatasets[intensity])
    return chartConfig

def adjustDayYsForDayAndName(SplitManager, data, day, name, intensities, lastIntensityData, dayYs):
    d = data[name]
    if day in d.keys():
        for intensity in intensities:
            if intensity not in dayYs.keys():
                dayYs[intensity] = []
            if intensity in d[day].keys():
                lastIntensityData[intensity] = 'null'
                watts = SplitManager.convertToWatts(d[day][intensity])
                dayYs[intensity].append(watts)
            else:
                dayYs[intensity].append(lastIntensityData[intensity])
    else:
        for intensity in dayYs.keys():
            dayYs[intensity].append(lastIntensityData[intensity])
    return dayYs, lastIntensityData

def avgOfList(l):
    s = 0
    t = 0
    for e in l:
        if isinstance(e, float):
            s += e
            t += 1
    if t == 0:
        return 'null'
    return round(s / t, 2)

def addBoatDatasets(data, xs, ColorHelper, ChartDataset, SplitManager, chartConfig, boat):
    intensityDatasets = getIntensityDatasets(ChartDataset)
    lastIntensityData = getFreshLastIntensityData()
    intensities = getIntensities()
    for day in xs:
        dayYs = {}
        for name in data.keys():
            dayYs, lastIntensityData = adjustDayYsForDayAndName(SplitManager, data, day, name, intensities, lastIntensityData, dayYs)
        for intensity in dayYs.keys():
            intensityDatasets[intensity].addData(avgOfList(dayYs[intensity]))
    for intensity in intensityDatasets.keys():
        intensityDatasets[intensity].addBackgroundColor(ColorHelper.getIntensityColor(intensity, 1.0))
        intensityDatasets[intensity].addBorderColor(ColorHelper.getIntensityColor(intensity, 1.0))
        intensityDatasets[intensity].setPointBorderColor(ColorHelper.getIntensityColor(intensity, 1.0))
        intensityDatasets[intensity].setPointBackgroundColor(ColorHelper.getIntensityColor(intensity, 1.0))
        intensityDatasets[intensity].setFill(False)
        intensityDatasets[intensity].setLabel(boat + " - " + intensity)
        intensityDatasets[intensity].setBorderWidth(3)
        chartConfig.addDataset(intensityDatasets[intensity])
    return chartConfig

def formatData(ChartConfig, ChartOptions, ChartDataset, ColorHelper, SplitManager, data, name):
    chartOptions = ChartOptions()
    chartOptions.setSpanGaps(True)
    chartConfig = ChartConfig('line', chartOptions)
    xs = getAllRelevantDays(data)
    chartConfig.setXAxisData(xs)
    chartConfig = addPersonDatasets(data[name], xs, ColorHelper, ChartDataset, SplitManager, chartConfig, name)
    return chartConfig.toJson()

def formatDataBoat(ChartConfig, ChartOptions, ChartDataset, ColorHelper, SplitManager, BoatManager, data, boat, peopleData):
    chartOptions = ChartOptions()
    chartOptions.setSpanGaps(True)
    chartConfig = ChartConfig('line', chartOptions)
    xs = getAllRelevantDays(data)
    chartConfig.setXAxisData(xs)
    peopleInBoat = BoatManager.getAllPeopleDataForBoat(peopleData, boat)
    boatData = {}
    for person in peopleInBoat:
        name = person["name"]
        if name in data.keys():
            boatData[name] = data[name]
    chartConfig = addBoatDatasets(boatData, xs, ColorHelper, ChartDataset, SplitManager, chartConfig, boat)
    return chartConfig.toJson()

def formatDataTeam(ChartConfig, ChartOptions, ChartDataset, ColorHelper, SplitManager, data, peopleData):
    chartOptions = ChartOptions()
    chartOptions.setSpanGaps(True)
    chartConfig = ChartConfig('line', chartOptions)
    xs = getAllRelevantDays(data)
    chartConfig.setXAxisData(xs)
    teamData = {}
    for person in peopleData:
        name = person["name"]
        if name in data.keys():
            teamData[name] = data[name]
    chartConfig = addBoatDatasets(teamData, xs, ColorHelper, ChartDataset, SplitManager, chartConfig, "Team")
    return chartConfig.toJson()
