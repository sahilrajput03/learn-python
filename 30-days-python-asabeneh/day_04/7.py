# index(): Returns the lowest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1). If the substring is not found it raises a valueError.
challenge = "thirty days of python"
sub_string = "da"
print(challenge.index(sub_string))  # 7

# print(challenge.index(sub_string, 9))  # runtime error
"""
ValueError: substring not found
"""


# rindex(): Returns the highest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1)
challenge = "thirty days of python"
sub_string = "da"
print(challenge.rindex(sub_string))  # 7
print(challenge.rindex("on", 8))  # 19

# print(challenge.rindex(sub_string, 9))  # runtime error
"""
ValueError: substring not found
"""
