# index(): Returns the lowest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1). If the substring is not found it raises a valueError.
challenge = "thirty days of python"
sub_string = "da"
print(challenge.index(sub_string))  # 7

try:
    # This statement throws runtime error: `ValueError: invalid literal for int() with base 10: '9.8'``
    print(challenge.index(sub_string, 9))
except ValueError:
    print("Got ValueError")  # Got ValueError
else:
    print("No exceptions occurred.")


# rindex(): Returns the highest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1)
challenge = "thirty days of python"
sub_string = "da"
print(challenge.rindex(sub_string))  # 7
print(challenge.rindex("on", 8))  # 19


try:
    # This statement throws runtime error: `ValueError: invalid literal for int() with base 10: '9.8'``
    print(challenge.rindex(sub_string, 9))
except ValueError:
    print("Got ValueError")  # Got ValueError
else:
    print("No exceptions occurred.")
