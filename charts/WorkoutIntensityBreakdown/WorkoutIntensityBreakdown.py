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


def populateDataset(data, name, ChartDataset, chartConfig):
    dataset = ChartDataset()
    for intensity in data.keys():
        dataset.addData(data[intensity])
        dataset.addBackgroundColor(getIntensityColor(intensity, 0.8))
        dataset.addBorderColor(getIntensityColor(intensity, 1.0))
        chartConfig.addLabel(intensity)
    chartConfig.addDataset(dataset)
    return chartConfig

def formatData(ChartConfig, ChartOptions, ChartDataset, data, name):
    chartOptions = ChartOptions()
    chartOptions.removeScales()
    chartConfig = ChartConfig('doughnut', chartOptions)
    chartConfig = populateDataset(data[name], name, ChartDataset, chartConfig)
    return chartConfig.toJson()
