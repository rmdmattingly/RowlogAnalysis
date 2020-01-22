class ChartDataset:

    def __init__(self):
        self.label = 'Default'
        self.data = []
        self.backgroundColor = []
        self.borderColor = []
        self.pointBackgroundColor = ''
        self.pointBorderColor = ''
        self.borderWidth = 1
        self.hidden = False
        self.fill = True

    def setLabel(self, label):
        self.label = label

    def addData(self, data):
        self.data.append(data)

    def addBackgroundColor(self, color):
        self.backgroundColor.append(color)

    def addBorderColor(self, color):
        self.borderColor.append(color)

    def setPointBackgroundColor(self, color):
        self.pointBackgroundColor = color

    def setPointBorderColor(self, color):
        self.pointBorderColor = color

    def setBorderWidth(self, width):
        self.borderWidth = width

    def setHidden(self, hidden):
        self.hidden = hidden

    def setFill(self, fill):
        self.fill = fill

    def toJson(self):
        return {
            "label": self.label,
            "data": self.data,
            "backgroundColor": self.backgroundColor,
            "borderColor": self.borderColor,
            "pointBackgroundColor": self.pointBackgroundColor,
            "pointBorderColor": self.pointBorderColor,
            "fill": self.fill,
            "borderWidth": self.borderWidth,
            "hidden": self.hidden
        }
