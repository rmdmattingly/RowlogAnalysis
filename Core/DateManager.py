from datetime import datetime, timedelta

formatString = '%Y-%m-%d'

# returns string, I know the name is misleading... refactor?
def fetchDateFromTimestampString(time):
    return time[0:10]

def getWorkoutsDataChronologically(workoutsData):
    return reversed(workoutsData)

# easy way to aggregate dates to a given week,
# also returns string because that cleans it up for output
def getMondayDateFromDate(dateStr):
    date = datetime.strptime(dateStr, formatString)
    wd = date.weekday()
    mon = date - timedelta(days=wd)
    return datetime.strftime(mon, formatString)
