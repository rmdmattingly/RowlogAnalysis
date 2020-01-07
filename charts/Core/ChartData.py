class ChartDataset:

    def __init__(self):
        self.label = 'Default'
        self.data = []
        self.backgroundColor = []
        self.borderColor = []
        self.borderWidth = 1
        self.hidden = False

    def setLabel(self, label):
        self.label = label

    def addData(self, data):
        self.data.append(data)

    def addBackgroundColor(self, color):
        self.backgroundColor.append(color)

    def addBorderColor(self, color):
        self.borderColor.append(color)

    def setBorderWidth(self, width):
        self.borderWidth = width

    def setHidden(self, hidden):
        self.hidden = hidden

    def toJson(self):
        return {
            "label": self.label,
            "data": self.data,
            "backgroundColor": self.backgroundColor,
            "borderColor": self.borderColor,
            "borderWidth": self.borderWidth,
            "hidden": self.hidden
        }
