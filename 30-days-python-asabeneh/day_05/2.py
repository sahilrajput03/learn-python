# checking items: Checking an item if it is a member of a list using in operator
fruits = ["banana", "orange", "mango", "lemon"]
print("banana" in fruits)  # True
print("lime" in fruits)  # False

print("--------- append(): To add item in the end of the list")
fruits = ["banana", "orange", "mango", "lemon"]
fruits.append("apple")
print(fruits)  # ['banana', 'orange', 'mango', 'lemon', 'apple']
fruits.append("lime")  # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime]
print(fruits)

print("\n--------- insert(): To add/put item at specified index")
fruits = ["banana", "orange", "mango", "lemon"]
# * Learn: insert() function expected 2 arguments else we get error - `TypeError: insert expected 2 arguments, got 1`
fruits.insert(2, "apple")  # insert apple between orange and mango
print(fruits)  # ['banana', 'orange', 'apple', 'mango', 'lemon']
fruits.insert(3, "lime")
print(fruits)  # ['banana', 'orange', 'apple', 'lime', 'mango','lemon']

print("\n--------- .remove(itemHere): Removing specified item from list")
fruits = ["banana", "orange", "mango", "lemon"]
fruits.remove("banana")
print(fruits)  # ['orange', 'mango', 'lemon']
fruits.remove("lemon")
print(fruits)  # ['orange', 'mango']

# .pop(): Remove last item (when no argument is specified) OR remove item at specified index
fruits = ["banana", "orange", "mango", "lemon"]
fruits.pop()
print(fruits)  # ['banana', 'orange', 'mango']

fruits.pop(0)  # remove item at index 0
print(fruits)  # ['orange', 'mango']

# del
print("\n--------- del")
fruits = ["banana", "orange", "mango", "lemon"]
del fruits[0]
print(fruits)  # ['orange', 'mango', 'lemon']
print("---------")

del fruits[1]
print(fruits)  # ['orange', 'lemon']

print("--------- DELETE THE ITEMS IN THE RANGE YOU SPECIFY")
fruits = ["banana", "orange", "mango", "lemon"]
# Deletes items between given indexes, so it does not delete the item with index 3!
del fruits[1:3]
print(fruits)  # ['banana', 'lemon']


del fruits  # to delete the list completely
# print(fruits)  # Throws: NameError: name 'fruits' is not defined

print("\n--------- clear")
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
