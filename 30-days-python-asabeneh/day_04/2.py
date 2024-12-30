# String Concatenation
first_name = "Asabeneh"
last_name = "Yetayeh"
space = " "
full_name = first_name + space + last_name
print(full_name)  # Asabeneh Yetayeh
print()

#### Unpacking characters
language = "Python"
a, b, c, d, e, f = language  # unpacking sequence characters into variables
print(a)  # P
print(b)  # y
print(c)  # t
print(d)  # h
print(e)  # o
print(f)  # n
print()

# Accessing characters in strings by index
language = "Python"
print(language[0])  # P
print(language[1])  # y
last_letter = language[len(language) - 1]
print(last_letter)  # n
print()

# If we want to start from right end we can use negative indexing. -1 is the last index
language = "Python"
# get last letter
print(language[-1])  # n
# get second last letter
print(language[-2])  # o
print()


# Slicing
language = "Python"
first_three = language[0:3]  # starts at zero index and up to 3 but not include 3
print(first_three)

last_three = language[3:6]
print(last_three)  # hon
# Another way
last_three = language[-3:]
print(last_three)  # hon
last_three = language[3:]
print(last_three)  # hon
print()

# Skipping character while splitting Python strings
language = "Python"
pto = language[0:6:2]  #
"""
Python's slice notation with three parameters: [start:end:step]
Let's break it down:
0 is the starting index
6 is the ending index (exclusive)
2 is the step (or stride) - meaning it takes every 2nd character
"""
print(pto)  # Pto
print()


# Escape sequence
print("I hope every one enjoying the python challenge.\nDo you ?")  # line break
# Output
"""
I hope every one enjoying the python challenge.
Do you ?
"""

print("Days\tTopics\tExercises")
print("Day 1\t3\t5")
print("Day 2\t3\t5")
print("Day 3\t3\t5")
print("Day 4\t3\t5")
print("This is a back slash  symbol (\\)")  # To write a back slash
print('In every programming language it starts with "Hello, World!"')
# Output
"""
Days	Topics	Exercises
Day 1	3	5
Day 2	3	5
Day 3	3	5
Day 4	3	5
This is a back slash  symbol (\)
In every programming language it starts with "Hello, World!"
"""
