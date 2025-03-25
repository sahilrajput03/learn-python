from datetime import date, datetime

# ex.1 - Format the current date using this format:
format = "%m/%d/%Y, %H:%M:%S"
currentDatetime = datetime.now()  # current date and time
print(currentDatetime.strftime(format))

# ex.3
# Today is 5 December, 2019. Change this time string to time
date_string = "5 December, 2019"
date_object = datetime.strptime(date_string, "%d %B, %Y")
print(date_object)  # 2019-12-05 00:00:00
print(type(date_object))  # <class 'datetime.datetime'>
