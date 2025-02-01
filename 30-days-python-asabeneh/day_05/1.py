# source -
# https://github.com/Asabeneh/30-Days-Of-Python/blob/master/05_Day_Lists/day_5.py

empty_list = list()  # this is an empty list, no item in the list
print(len(empty_list))  # 0
print(len(empty_list) == 0)  # True

# Lists can have items of different data types
lst = [
    "Asabeneh",
    250,
    True,
    {"country": "Finland", "city": "Helsinki"},
]

# sq bracket syntax
fruits = ["banana", "orange", "mango", "lemon"]  # list of fruits
print(fruits)  #  ['banana', 'orange', 'mango', 'lemon']
print(len(fruits))  # 4
print(fruits[0])  # banana
print(fruits[1])  # orange
print(fruits[len(fruits) - 1])  # lemon
print(fruits[-2])  # mango (accessing second last item)

# ---- Slicing items ----
fruits = ["banana", "orange", "mango", "lemon"]
print(fruits[0:4])  # returns all the fruits

#  If we don't set where to stop it takes all the rest
print(fruits[0:])  # returns all the fruits as above

# exclude first item and the last item (Note: item at index 3 is excluded)
print(fruits[1:3])  # ['orange', 'mango']
print(fruits[1:])  # ['orange', 'mango', 'lemon']

fruits = ["banana", "orange", "mango", "lemon"]
all_fruits = fruits[-4:]  # it returns all the fruits
# this is also give the same result as the above
orange_and_mango = fruits[-3:-1]  # it does not include the end index
print(orange_and_mango)  # ['orange', 'mango']

orange_mango_lemon = fruits[-3:]
print(orange_mango_lemon)  # ['orange', 'mango', 'lemon']


# --- Modifying ---
fruits = ["banana", "orange", "mango", "lemon"]
fruits[0] = "Avocado"
print(fruits)  #  ['avocado', 'orange', 'mango', 'lemon']
fruits[1] = "apple"
print(fruits)  #  ['avocado', 'apple', 'mango', 'lemon']
last_index = len(fruits) - 1
fruits[last_index] = "lime"
print(fruits)  #  ['avocado', 'apple', 'mango', 'lime']
