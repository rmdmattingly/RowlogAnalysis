import math

def calcSeconds(min, sec):
    return (float(min) * 60) + float(sec)

def parseStringToMinAndSec(splitTime):
    minsAndSecArr = splitTime.split(':')
    return minsAndSecArr[0], minsAndSecArr[1]
    
# call this function to convert a split like 1:30.6 to seconds 90.6 -- makes it easier to rank by split
def convertSplitToSeconds(splitTime):
    min, sec = parseStringToMinAndSec(splitTime)
    return calcSeconds(min, sec)

# call this function to convert seconds like 95.6 to a split 1:35.6 -- makes it easier to display data
def convertSecondsToSplit(sec):
    min = int(math.floor(float(sec) / 60))
    sec = round(float(sec) - (min*60), 1)
    if (sec < 10):
        sec = '0' + str(sec)
    return str(min) + ':' + str(sec)
