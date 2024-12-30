## String Methods
# capitalize(): Converts the first character the string to Capital Letter
challenge = "thirty days of python"
print(challenge.capitalize())  # 'Thirty days of python'

# count(): returns occurrences of substring in string, count(substring, start=.., end=..)

challenge = "thirty days of python"
print(challenge.count("y"))  # 3
print(challenge.count("y", 7, 14))  # 1
print(challenge.count("th"))  # 2`

# endswith(): Checks if a string ends with a specified ending

challenge = "thirty days of python"
print(challenge.endswith("on"))  # True
print(challenge.endswith("tion"))  # False

# expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument
# By default the \t expands to 8 spaces
challenge = "thirty\tdays\tof\tpython"
print(challenge)
print(challenge.expandtabs())  # 'thirty  days    of      python'
# We can pass how many spaces to use for tabs by passing argument
print(challenge.expandtabs(10))  # 'thirty    days      of        python'

# find(): Returns the index of first occurrence of substring
challenge = "thirty days of python"
print(challenge.find("y"))  # 5
print(challenge.find("th"))  # 0
print()


# rfind(): Returns the index of the last occurrence of a substring, if not found returns -1
challenge = "thirty days of python"
print(challenge.rfind("y"))  # 16
print(challenge.rfind("th"))  # 17


# index(): Returns the index of substring
challenge = "thirty days of python"
print(challenge.find("y"))  # 5
print(challenge.find("th"))  # 0

# isalnum(): Checks alphanumeric character
challenge = "ThirtyDaysPython"
print(challenge.isalnum())  # True

challenge = "30DaysPython"
print(challenge.isalnum())  # True

challenge = "thirty days of python"
print(challenge.isalnum())  # False

challenge = "thirty days of python 2019"
print(challenge.isalnum())  # False

# isalpha(): Checks if all characters are alphabets
challenge = "thirty days of python"
print(challenge.isalpha())  # True
num = "123"
print(num.isalpha())  # False
