class ChartServiceParams:
    def __init__(self, field, required):
        self.field = field
        self.required = required

    def toJson(self):
        return {
            "field": self.field,
            "required": self.required
        }
        