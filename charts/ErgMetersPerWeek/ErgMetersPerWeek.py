def getDataset(data, ChartDataset, ColorHelper):
    dataset = ChartDataset()
    dataset.addBackgroundColor(ColorHelper.generateRandomRgbaColor(0.0))
    dataset.addBorderColor(ColorHelper.generateRandomRgbaColor(1.0))
    for week in data.keys():
        dataset.addData(data[week])
        
    return dataset
    
def formatData(ChartConfig, ChartOptions, ChartDataset, ColorHelper, data):
    chartConfig = ChartConfig('line', ChartOptions())
    chartConfig.setXAxisData(data.keys())
    chartConfig.addDataset(getDataset(data, ChartDataset, ColorHelper))
    return chartConfig.toJson()
