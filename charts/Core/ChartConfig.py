class ChartConfig:
    def __init__(self, type, options):
        self.type = type
        self.data = {
            'data': [],
            'labels': []
        }
        self.options = options

    def addDataset(self, dataset):
        self.data['data'].append(dataset)

    def setXAxisData(self, xAxisPoints):
        self.data['labels'] = xAxisPoints

    def __jsonifyData(self):
        jsonifiedDatasets = []
        for dataset in self.data['data']:
            jsonifiedDatasets.append(dataset.toJson())
        return jsonifiedDatasets

    def toJson(self):
        return {
            "type": self.type,
            "options": self.options.toJson(),
            "data": {
                "labels": self.data['labels'],
                "datasets": self.__jsonifyData()
            }
        }
