# isdigit(): Checks if all characters in a string are numbers (0-9 and some other unicode characters for numbers)
print("Thirty".isdigit())  # False
print("30".isdigit())  # True
print("\u00B2")  # ²
print("\u00B2".isdigit())  # True
print()

# isdecimal(): Checks if all characters in a string are decimal (0-9)
print("isdecimal()")
print("10".isdecimal())  # True
print("10.5".isdecimal())  # False
print("thirty days of python".isdecimal())  # False
print("123".isdecimal())  # True
print("12 3".isdecimal())  # False, space not allowed
print()


# isidentifier():Checks for valid identifier means it check if a string is a valid variable name
challenge = "30DaysOfPython"
print(challenge.isidentifier())  # False, because it starts with a number
challenge = "thirty_days_of_python"
print(challenge.isidentifier())  # True


# islower():Checks if all alphabets in a string are lowercase
challenge = "thirty days of python"
print(challenge.islower())  # True
challenge = "Thirty days of python"
print(challenge.islower())  # False

# isupper(): returns if all characters are uppercase characters
challenge = "thirty days of python"
print(challenge.isupper())  #  False
challenge = "THIRTY DAYS OF PYTHON"
print(challenge.isupper())  # True
print()


# isnumeric():Checks numeric characters
print("isnumeric()")
num = "10"
print(num.isnumeric())  # True
print("ten".isnumeric())  # False
num = "\u00BD"  # ½
print(num)
print(num.isnumeric())  # True
num = "10.5"
print(num.isnumeric())  # False
