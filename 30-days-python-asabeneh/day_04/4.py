# isdigit(): Checks Digit Characters
print("Thirty".isdigit())  # False
print("30".isdigit())  # True

# isdecimal():Checks decimal characters
print("10".isdecimal())  # True
print("10.5".isdecimal())  # False

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


# isnumeric():Checks numeric characters
num = "10"
print(num.isnumeric())  # True
print("ten".isnumeric())  # False
