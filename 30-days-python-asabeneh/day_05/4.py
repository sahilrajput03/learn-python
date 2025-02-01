# checking items
fruits = ["banana", "orange", "mango", "lemon"]
print("banana" in fruits)  # True
print("lime" in fruits)  # False

# Append
fruits = ["banana", "orange", "mango", "lemon"]
fruits.append("apple")
print(fruits)  # ['banana', 'orange', 'mango', 'lemon', 'apple']
fruits.append("lime")  # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime]
print(fruits)
print("---------")

# Insert
fruits = ["banana", "orange", "mango", "lemon"]
fruits.insert(2, "apple")  # insert apple between orange and mango
print(fruits)  # ['banana', 'orange', 'apple', 'mango', 'lemon']
fruits.insert(3, "lime")
print(fruits)  # ['banana', 'orange', 'apple', 'lime', 'mango','lemon']
print("---------")

# Remove
fruits = ["banana", "orange", "mango", "lemon"]
fruits.remove("banana")
print(fruits)  # ['orange', 'mango', 'lemon']
fruits.remove("lemon")
print(fruits)  # ['orange', 'mango']
print("---------")

# pop (removes the last item if no argument is supplied)
fruits = ["banana", "orange", "mango", "lemon"]
fruits.pop()
print(fruits)  # ['banana', 'orange', 'mango']

fruits.pop(0)  # remove item at index 0
print(fruits)  # ['orange', 'mango']
print("---------")

# del
fruits = ["banana", "orange", "mango", "lemon"]
del fruits[0]
print(fruits)  # ['orange', 'mango', 'lemon']
print("---------")

del fruits[1]
print(fruits)  # ['orange', 'lemon']
del fruits
# print(fruits)  # Throws: NameError: name 'fruits' is not defined
print("---------")


# clear
fruits = ["banana", "orange", "mango", "lemon"]
fruits.clear()
print(fruits)  # []
print("---------")

# copying a lits
fruits = ["banana", "orange", "mango", "lemon"]
fruits_copy = fruits.copy()
fruits_copy.append("apple")
print(fruits)  # ['banana', 'orange', 'mango', 'lemon']
print(fruits_copy)  # ['banana', 'orange', 'mango', 'lemon', 'apple']
print("---------")


# join - example 1
positive_numbers = [1, 2, 3]
zero = [0]
negative_numbers = [-3, -2, -1]
integers = negative_numbers + zero + positive_numbers
print(integers)  # [-3, -2, -1, 0, 1, 2, 3]
print("---------")


# join - example 2
fruits = ["banana", "orange", "mango", "lemon"]
vegetables = ["Tomato", "Potato", "Cabbage", "Onion", "Carrot"]
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)


# join with extend - `list1.extend(list2)`
num1 = [0, 1, 2, 3]
num2 = [4, 5, 6]
num1.extend(num2)
print(num1)  #  [0, 1, 2, 3, 4, 5, 6]
print("---------")


# count
fruits = ["banana", "orange", "mango", "lemon"]
print(fruits.count("orange"))  # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))  # 3
print("---------")

# index
fruits = ["banana", "orange", "mango", "lemon"]
print(fruits.index("orange"))  # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
# returns the index of first encountered matching item
print(ages.index(24))  # 2
print("---------")


# Reverse - example 1
fruits = ["banana", "orange", "mango", "lemon"]
fruits.reverse()
print(fruits)  # ['lemon', 'mango', 'orange', 'banana']

# Reverse - example 2
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages)  # [24, 25, 24, 26, 25, 24, 19, 22]


# Sort
fruits = ["banana", "orange", "mango", "lemon"]
# alphabetical sort
fruits.sort()
print(fruits)  # ['banana', 'lemon', 'mango', 'orange']

# alphabetical reverse sort
fruits.sort(reverse=True)  # ['orange', 'mango', 'lemon', 'banana']
print(fruits)

ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages)  # [19, 22, 24, 24, 24, 25, 25, 26]

ages.sort(reverse=True)
print(ages)  # [26, 25, 25, 24, 24, 24, 22, 19]
