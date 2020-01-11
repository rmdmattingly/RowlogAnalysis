class ChartServiceParams:
    def __init__(self, field, required):
        self.field = field
        self.required = required

    def getField(self):
        return self.field

    def toJson(self):
        return {
            "field": self.field,
            "required": self.required
        }
        