def getIntensityColor(intensity, transparency):
    intensityToColor = {
        "U3": 'rgba({}, {}, {}, {})'.format(0, 128, 255, transparency),
        "U2": 'rgba({}, {}, {}, {})'.format(0, 255, 255, transparency),
        "U1": 'rgba({}, {}, {}, {})'.format(0, 255, 0, transparency),
        "AT": 'rgba({}, {}, {}, {})'.format(255, 255, 0, transparency),
        "TR": 'rgba({}, {}, {}, {})'.format(255, 128, 0, transparency),
        "Test": 'rgba({}, {}, {}, {})'.format(255, 0, 0, transparency)
    }
    return intensityToColor[intensity]

def createDonutChart(titleText, ChartConfig, ChartOptions):
    chartOptions = ChartOptions()
    chartOptions.removeScales()
    chartOptions.setTitleText(titleText)
    return ChartConfig('doughnut', chartOptions)

def populateDataset(data, ChartDataset, chartConfig):
    dataset = ChartDataset()
    for intensity in data.keys():
        dataset.addData(data[intensity])
        dataset.addBackgroundColor(getIntensityColor(intensity, 0.8))
        dataset.addBorderColor(getIntensityColor(intensity, 1.0))
        chartConfig.addLabel(intensity)
    chartConfig.addDataset(dataset)
    return chartConfig

def populateTeamDataset(data, ChartDataset, chartConfig):
    intensityCounts = {
        "U3": 0,
        "U2": 0,
        "U1": 0,
        "AT": 0,
        "TR": 0,
        "Test": 0
    }
    total = 0
    for person in data.keys():
        for intensity in data[person]:
            if intensity in intensityCounts.keys():
                intensityCounts[intensity] += 1
                total += 1
    return populateDataset(intensityCounts, ChartDataset, chartConfig)

def formatData(ChartConfig, ChartOptions, ChartDataset, data, name):
    chartConfig = createDonutChart("Workout Intensity Breakdown - " + name, ChartConfig, ChartOptions)
    chartConfig = populateDataset(data[name], ChartDataset, chartConfig)
    return chartConfig.toJson()

def formatDataTeam(ChartConfig, ChartOptions, ChartDataset, data):
    chartConfig = createDonutChart("Workout Intensity Breakdown - Team", ChartConfig, ChartOptions)
    chartConfig = populateTeamDataset(data, ChartDataset, chartConfig)
    return chartConfig.toJson()
