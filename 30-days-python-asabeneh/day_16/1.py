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
now = datetime.now()
print(now)  # 2025-03-25 20:26:48.087765
print(now.day)  # 25
print(now.month)  # 3
print(now.year)  # 2025
print(now.hour)  # 20
print(now.minute)  # 27
print(now.second)  # 10
# Timestamp or Unix timestamp is the number of seconds elapsed from 1st of January 1970 UTC
print(now.timestamp())  # 1742914630.235397

print("\n\nPassing argument to datetime(..)")
new_year = datetime(2020, 1, 1)
print(new_year)
# Output: 2020-01-01 00:00:00

print(
    new_year.day,
    new_year.month,
    new_year.year,
    new_year.hour,
    new_year.minute,
    new_year.second,
)
# Output: 1 1 2020 0 0 0

print(
    f"{new_year.day}/{new_year.month}/{new_year.year}, {new_year.hour}:{new_year.minute}:{new_year.second}"
)
# Output: 1/1/2020, 0:0:0
