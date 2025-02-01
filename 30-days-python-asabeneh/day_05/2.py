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

# copying a list
fruits = ["banana", "orange", "mango", "lemon"]
fruits_copy = fruits.copy()
fruits_copy.append("apple")
print(fruits)  # ['banana', 'orange', 'mango', 'lemon']
print(fruits_copy)  # ['banana', 'orange', 'mango', 'lemon', 'apple']
print("---------")
