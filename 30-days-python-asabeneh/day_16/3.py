from datetime import date, datetime

####### * Difference Between Two Points in Time ########
today = date(year=2019, month=12, day=5)
new_year = date(year=2020, month=1, day=1)

time_left_for_newyear = new_year - today

# print(type(time_left_for_newyear))  # <class 'datetime.timedelta'>
print("Time left for new year: ", time_left_for_newyear)  # 27 days, 0:00:00

t1 = datetime(year=2019, month=12, day=5, hour=0, minute=59, second=0)
t2 = datetime(year=2020, month=1, day=1, hour=0, minute=0, second=0)
diff = t2 - t1

print("Time left for new year:", diff)  # 26 days, 23:01:00


####### * Difference Between Two Points in Time via timedelta function
from datetime import timedelta

t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3 =", t3)  #  86 days, 22:56:50
