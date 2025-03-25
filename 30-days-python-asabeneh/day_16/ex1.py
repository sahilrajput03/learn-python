from datetime import date, datetime, timedelta

# ex.1: Format the current date using this format:
format = "%m/%d/%Y, %H:%M:%S"
currentDatetime = datetime.now()  # current date and time
print(currentDatetime.strftime(format))

# ex.3: Today is 5 December, 2019. Change this time string to time
datetimeString = "5 December, 2019"
datetimeNow = datetime.strptime(datetimeString, "%d %B, %Y")
print(datetimeNow)  # 2019-12-05 00:00:00
print(type(datetimeNow))  # <class 'datetime.datetime'>

# ex.4 Calculate the time difference between now and new year.
datetimeNow = datetime.now()
# (arguments order: year, month, day, hour, minute, second, microsecond)
datetimeNewYear1 = datetime(2026, 1, 1)
datetimeNewYear2 = datetime(year=2026, month=1, day=1, hour=0, minute=0, second=0)

print(datetimeNewYear1 - datetimeNow)  # way1
print(datetimeNewYear2 - datetimeNow)  # way2


# ex.5 Calculate the time difference between 1 January 1970 and now
datetimeNow = datetime.now()
datetime1970 = datetime(1970, 1, 1)
print(datetimeNow - datetime1970)
