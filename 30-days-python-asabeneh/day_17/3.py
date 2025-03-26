# & Packing and Unpacking Arguments in Python
# & We use two operators:
# &     1. Python uses * for tuples
# &     2. Python uses ** for dictionaries


def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e


lst = [1, 2, 3, 4, 5]

# Below instruction throws: TypeError: sum_of_five_nums() missing 4 required positional arguments: 'b', 'c', 'd', and 'e'
# print(sum_of_five_nums(lst))

# unpack/destructure the list
print(sum_of_five_nums(*lst))

# Destructuting/Unpacking `range(..)`
numbers = range(2, 7)  # normal call with separate arguments
print(numbers)  # range(2, 7)
print(list(numbers))  # [2, 3, 4, 5, 6]

# Passing list (array) of values as `args` to function via destructuting/unpacking
args = [2, 7]
numbers = range(*args)  # call with arguments unpacked from a list
print(numbers)  # [2, 3, 4, 5,6]


# * list destructuring/unpacking
countries = ["Finland", "Sweden", "Norway", "Denmark", "Iceland"]
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest)  # Finland Sweden Norway ['Denmark', 'Iceland']

# * tuple destructuring/unpacking
numbers = (1, 2, 3, 4, 5, 6, 7)
one, *middle, last = numbers
print(one, middle, last)  #  1 [2, 3, 4, 5, 6] 7


# * Unpacking Dictionaries
def unpacking_person_info(name, country, city, age):
    return f"{name} lives in {country}, {city}. He is {age} year old."


dct = {"name": "Sahil", "country": "India", "city": "Chandigarh", "age": 250}
print(unpacking_person_info(**dct))
# Output Sahil lives in India, Chandigarh. He is 1750 years old.


# * Packing Dictionaries
def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s


print(sum_all(1, 2, 3))  # 6
print(sum_all(1, 2, 3, 4, 5, 6, 7))  # 28


# & Packing Dictionaries
# `kwargs` stands for "keyword arguments"
# * Learn: Appening ** before an argument allows a function to accept any number of keyword arguments
def packing_person_info(**kwargs):
    print(type(kwargs))  # <class 'dict'>
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    return kwargs


# Passing keyword arguments to function call:
print(packing_person_info(name="Asabeneh", country="Finland", city="Helsinki", age=250))

# * List Spreading (like spreading in javascript)
lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *lst_one, *lst_two]
print(lst)  # [0, 1, 2, 3, 4, 5, 6, 7]

country_lst1 = ["Finland", "Sweden", "Norway"]
country_lst2 = ["Denmark", "Iceland"]
nordic_countries = [*country_lst1, *country_lst2]
print(nordic_countries)  # ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']


# * Enumerate
# If we are interested in an index of a list, we use `enumerate ()` built-in function to get the index of each item in the list.

for index, item in enumerate([20, 30, 40]):
    print(index, item)
    # Output:
    # 0 20
    # 1 30
    # 2 40

countries = ["Finland", "Sweden", "Norway", "Denmark", "Iceland"]
for index, country in enumerate(countries):
    print("hi", index)
    if country == "Finland":
        print(f"The country {country} has been found at index {index}")
        # Output:
        # hi 0
        # The country Finland has been found at index 0
        # hi 1
        # hi 2
        # hi 3
        # hi 4


# * Zip - To loop over two lists using a single for loop instead of two nested for loops
fruits = ["banana", "orange"]
veges = ["Tomato", "Potato"]  # (vegetables)
fruits_and_veges = []
for fruit, veg in zip(fruits, veges):
    fruits_and_veges.append({"fruit": fruit, "veg": veg})
print(fruits_and_veges)
# [{'fruit': 'banana', 'veg': 'Tomato'}, {'fruit': 'orange', 'veg': 'Potato'}]

# Doing above functioning without using `zip`
fruits_and_veges = []
for i in range(len(fruits)):
    fruits_and_veges.append({"fruit": fruits[i], "veg": veges[i]})
print(fruits_and_veges)
# [{'fruit': 'banana', 'veg': 'Tomato'}, {'fruit': 'orange', 'veg': 'Potato'}]
