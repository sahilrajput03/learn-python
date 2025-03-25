from datetime import datetime, date


# Learn `strptime` function
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
