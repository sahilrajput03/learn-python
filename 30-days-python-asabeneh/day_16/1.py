import datetime  # `datetime` module to handle date and time

# Using `dir` or `help` built-in commands it is possible to know the available
#       functions in a certain module
print(dir(datetime))
[
    "MAXYEAR",
    "MINYEAR",
    "__builtins__",
    "__cached__",
    "__doc__",
    "__file__",
    "__loader__",
    "__name__",
    "__package__",
    "__spec__",
    "date",
    "datetime",
    "datetime_CAPI",
    "sys",
    "time",
    "timedelta",
    "timezone",
    "tzinfo",
]

print("")

from datetime import datetime

# We will learn about --- date, datetime, time and timedelta function from above:
datetimeNow = datetime.now()  # <class 'datetime.datetime'>
print(type(datetimeNow))
print(datetimeNow)  # 2025-03-25 20:26:48.087765
print(datetimeNow.day)  # 25
print(datetimeNow.month)  # 3
print(datetimeNow.year)  # 2025
print(datetimeNow.hour)  # 20
print(datetimeNow.minute)  # 27
print(datetimeNow.second)  # 10
# Timestamp or Unix timestamp is the number of seconds elapsed from 1st of January 1970 UTC
print(datetimeNow.timestamp())  # 1742914630.235397

print("\n\nPassing argument to datetime(..)")
newYear = datetime(2020, 1, 1)
print(newYear)
# Output: 2020-01-01 00:00:00

print(
    newYear.day,
    newYear.month,
    newYear.year,
    newYear.hour,
    newYear.minute,
    newYear.second,
)
# Output: 1 1 2020 0 0 0

print(
    f"{newYear.day}/{newYear.month}/{newYear.year}, {newYear.hour}:{newYear.minute}:{newYear.second}"
)
# Output: 1/1/2020, 0:0:0
