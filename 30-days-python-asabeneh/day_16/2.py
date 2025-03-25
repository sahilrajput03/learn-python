from datetime import datetime, date, time

# * 🚀 Learn strftime Docs: https://strftime.org/
now = datetime.now()  # current date and time

print(type(now.strftime("%H:%M:%S")))  # <class 'str'>

print("H:M:S:", now.strftime("%H:%M:%S"))
# Output: H:M:S: 20:39:24

print("mm/dd/YY H:M:S", now.strftime("%m/%d/%Y, %H:%M:%S"))
# Output: mm/dd/YY H:M:S 03/25/2025, 20:39:24

print("dd/mm/YY H:M:S", now.strftime("%d/%m/%Y, %H:%M:%S"))
# Output: dd/mm/YY H:M:S 25/03/2025, 20:39:24

print("\n\n--------------------------------")

# * 🚀 Learn `strptime` function
date_string = "5 December, 2019"
date_object = datetime.strptime(date_string, "%d %B, %Y")
print(type(date_object))  # <class 'datetime.datetime'>
print(date_object)  # 2019-12-05 00:00:00


print("----------------- ")

d = date(2020, 1, 1)
print(d)  # 2020-01-01
print("Current date:", d.today())  # 2025-03-25
print(type(d.today()))  # <class 'datetime.date'>

# date object of today's date #
today = date.today()
print("\nCurrent year:", today.year)  # 2025
print("Current month:", today.month)  # 3
print("Current day:", today.day)  # 25


# * 🚀 Learn `time` function
# Default time: 00:00:00:00 (hour:minute:second:microsecond)
a = time()
print("a =", a)  # 00:00:00
print(type(a))  # <class 'datetime.time'>

b = time(10, 30, 50)
print("b =", b)  # 10:30:50

c = time(hour=10, minute=30, second=50)
print("c =", c)  # 10:30:50

# Passsing Arguments: time(hour, minute, second, microsecond)
d = time(10, 30, 50, 200555)
print("d =", d)  # 10:30:50.200555
