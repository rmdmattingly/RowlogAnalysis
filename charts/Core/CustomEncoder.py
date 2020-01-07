class CustomEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, ChartConfig):
            return {
                "type": obj.type,
                "data": obj.data,
                "options": default(self, obj.options)
            }
        if isinstance(obj, ChartData):
            return {
                "type": obj.type,
                "data": obj.data,
                "options": default(self, obj.options)
            }
        return json.JSONEncoder.default(self, obj)