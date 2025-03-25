from datetime import datetime

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
