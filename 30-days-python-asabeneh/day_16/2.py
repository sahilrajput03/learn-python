from datetime import datetime, date, time

# * 🚀 Learn strftime - To parse datetime from string
# Docs: https://strftime.org/
#       The full set of format codes supported varies across
#       platforms, because Python calls the platform C
#       library's strftime() function, and platform
#       variations are common.
# * Linux C Library Docs of strftime (from above docs page):
#       https://man7.org/linux/man-pages/man3/strftime.3.html

datetimeNow = datetime.now()  # current date and time

print(type(datetimeNow.strftime("%H:%M:%S")))  # <class 'str'>

print("H:M:S:", datetimeNow.strftime("%H:%M:%S"))
# Output: H:M:S: 20:39:24

print("mm/dd/YY H:M:S", datetimeNow.strftime("%m/%d/%Y, %H:%M:%S"))
# Output: mm/dd/YY H:M:S 03/25/2025, 20:39:24

print("dd/mm/YY H:M:S", datetimeNow.strftime("%d/%m/%Y, %H:%M:%S"))
# Output: dd/mm/YY H:M:S 25/03/2025, 20:39:24

print("\n\n--------------------------------")

# * 🚀 Learn `strptime` function
datetimeString = "5 December, 2019"
datetime1 = datetime.strptime(datetimeString, "%d %B, %Y")
print(type(datetime1))  # <class 'datetime.datetime'>
print(datetime1)  # 2019-12-05 00:00:00


print("----------------- ")

time1 = date(2020, 1, 1)
print(time1)  # 2020-01-01
print("Current date:", time1.today())  # 2025-03-25
print(type(time1.today()))  # <class 'datetime.date'>

# date object of today's date #
datetimeToday = date.today()
print("\nCurrent year:", datetimeToday.year)  # 2025
print("Current month:", datetimeToday.month)  # 3
print("Current day:", datetimeToday.day)  # 25


# * 🚀 Learn `time` function
# Default time: 00:00:00:00 (hour:minute:second:microsecond)
time1 = time()
print("a =", time1)  # 00:00:00
print(type(time1))  # <class 'datetime.time'>

time1 = time(10, 30, 50)
print("b =", time1)  # 10:30:50

time1 = time(hour=10, minute=30, second=50)
print("c =", time1)  # 10:30:50

# Passsing Arguments: time(hour, minute, second, microsecond)
time1 = time(10, 30, 50, 200555)
print("d =", time1)  # 10:30:50.200555
