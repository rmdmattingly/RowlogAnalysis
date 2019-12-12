#Events have a summary, and decription as well as some others but those are most important
def getRecomendedWorkout():
    from datetime import timedelta
    from icalevents.icalevents import events
    cal  = events('https://api.band.us/ical?token=aAAxADYxZDhkNzk0ZmFiOWFkMTA1Njk1MzZkMTczN2MwNzU2YzY2YWE1Nzg', end=timedelta(days=0))
    for event in cal:
        if event.summary != "Core" and event.summary != "Lift":
            return event
