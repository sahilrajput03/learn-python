# List comprehension in Python is a compact way of creating a list from a sequence
# *syntax*
# [i for i in iterable if expression]


# * Converting string to list comprehension
# * 1st Way
language = "Python"
lst = list(language)  # changing the string to list
print(type(lst))  # list
print(lst)  # ['P', 'y', 't', 'h', 'o', 'n']

# * 2nd Way
lst = [i for i in language]
print(type(lst))  # list
print(lst)  # ['P', 'y', 't', 'h', 'o', 'n']


# Learn: Range is not a primitive data type but a "class"
print(type(range(11)))  # "range" type
if isinstance(range(11), range):
    print("range type")

# #################
# Generating numbers
numbers = [i for i in range(11)]  # to generate numbers from 0 to 10
print(numbers)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# It is possible to do mathematical operations during iteration
squares = [i * i for i in range(11)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Learn: From Sahil: This is like map in javascript. This way we create tuples form a list:
numbers = [(i, i * i) for i in range(11)]
print(numbers)  # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
