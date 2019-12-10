import datetime
import time
from datetime import date
from datetime import timedelta

def getCurrentWeek(date):
     startDate = getMondayBeforeDate(date)
     endDate = getSundayAfterDate(date)
     return startDate, endDate

##gets last monday 
def getMondayBeforeDate(date):
     today = datetime.date.today()
     last_monday = today - datetime.timedelta(days=today.weekday())

##gets next monday
def getMondayNextDate(date):
     today = datetime.date.today()
     coming_monday = today + datetime.timedelta(days=-today.weekday(), weeks=1) 

##gets last Sunday     
def getSundayAfterDate(date):
     idx = (today.weekday() + 1) % 7
     sun = today - datetime.timedelta(7+idx)

##gets most recent Sunday
def getSundayDate(date):
     today = datetime.date.today()
     weekday = today.weekday() + 1
     start_day = today - datetime.timedelta(days=weekday % 7)
     
