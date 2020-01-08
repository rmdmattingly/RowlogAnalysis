class ChartService:
    def __init__(self, chartServiceName, analysisServiceName, readableName):
        self.chartServiceName = chartServiceName
        self.analysisServiceName = analysisServiceName
        self.readableName = readableName

    def getChartServiceName(self):
        return self.chartServiceName

    def toJson(self):
        return {
            "chartServiceName": self.chartServiceName,
            "analysisServiceName": self.analysisServiceName,
            "readableName": self.readableName
        }
