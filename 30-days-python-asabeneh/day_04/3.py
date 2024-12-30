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
challenge = "thirty\tdays\tof\tpython"
print(challenge.expandtabs())  # 'thirty  days    of      python'
print(challenge.expandtabs(10))  # 'thirty    days      of        python'

# find(): Returns the index of first occurrence of substring
challenge = "thirty days of python"
print(challenge.find("y"))  # 5
print(challenge.find("th"))  # 0

# format()	formats string into nicer output
first_name = "Asabeneh"
last_name = "Yetayeh"
job = "teacher"
country = "Finland"
sentence = "I am {} {}. I am a {}. I live in {}.".format(
    first_name, last_name, job, country
)
print(sentence)  # I am Asabeneh Yetayeh. I am a teacher. I live in Finland.
print()


radius = 10
pi = 3.14
area = pi  # radius ## 2
result = "The area of circle with {} is {}".format(str(radius), str(area))
print(result)  # The area of circle with 10 is 314.0
result = "The area of circle with {} is {}".format(radius, area)
print(result)  # The area of circle with 10 is 314.0


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
