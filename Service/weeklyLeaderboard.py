import datetime
import time
from datetime import date, timedelta

def getCurrentStartDate(date):
     startDate = getMondayBeforeDate(date)
     return startDate

def getCurrentEndDate(date):
     endDate = getSundayAfterDate(date)
     return endDate

def getWeeklyMeters(workoutData):
     totalWeeklyMeters = []
     startDate = getCurrentStartDate(date)
     end = getCurrentEndDate(date)
     for workout in workoutData:
          if workout['time'] > startDate.time() and workout['time'] < endDate.time()
          totalWeeklyMeters[workout['people-id']] += workout['scored_meters']
          return totalWeelyMeters
     
##gets last monday 
def getMondayBeforeDate(date):
     today = datetime.date.today()
     lastMonday = today - datetime.timedelta(days=today.weekday())
     return lastMonday

##gets last Sunday     
def getSundayAfterDate(date):
     idx = (today.weekday() + 1) % 7
     lastSunday = today - datetime.timedelta(7+idx)
     return lastSunday

def run(workoutData):
     return getWeeklyMeters(workoutData)
     
