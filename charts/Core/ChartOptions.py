class ChartOptions:
    def __init__(self):
        self.responsive = True
        self.title = {
            "display": True,
            "text": "Select an Item in the Legend to Include it on the Chart"
        }
        self.tooltips = {
            "mode": "nearest",
            "intersect": False
        }
        self.hover = {
            "mode": "nearest",
            "intersect": "false"
        }
        self.scales = {
            'yAxes': [{
                'ticks': {
                    'beginAtZero': True
                }
            }]
        }
        self.spanGaps = False

    def removeScales(self):
        self.scales = {}

    def setTitleText(self, text):
        self.title["text"] = text

    def setSpanGaps(self, spanGaps):
        self.spanGaps = spanGaps

    def toJson(self):
        return {
            "responsive": self.responsive,
            "title": self.title,
            "tooltips": self.tooltips,
            "hover": self.hover,
            "scales": self.scales,
            "spanGaps": self.spanGaps
        }
