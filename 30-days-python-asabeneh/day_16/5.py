from datetime import time

# Learn `time` function

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
