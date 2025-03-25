# 🚀 strftime Docs: https://strftime.org/
from datetime import datetime

now = datetime.now()  # current date and time

print(type(now.strftime("%H:%M:%S")))  # <class 'str'>

print("H:M:S:", now.strftime("%H:%M:%S"))
# Output: H:M:S: 20:39:24

print("mm/dd/YY H:M:S", now.strftime("%m/%d/%Y, %H:%M:%S"))
# Output: mm/dd/YY H:M:S 03/25/2025, 20:39:24

print("dd/mm/YY H:M:S", now.strftime("%d/%m/%Y, %H:%M:%S"))
# Output: dd/mm/YY H:M:S 25/03/2025, 20:39:24
