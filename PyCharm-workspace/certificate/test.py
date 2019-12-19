import datetime

what_week = datetime.datetime.now().weekday()
if what_week == 6:
    day = datetime.datetime.now()
    createDt = day.strftime('%Y%m%d')
    print(createDt)
else:
    day = datetime.datetime.now() - datetime.timedelta(days=what_week+1)
    createDt = day.strftime('%Y%m%d')
    print(createDt)