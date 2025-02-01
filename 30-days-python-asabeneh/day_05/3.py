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
print(ages.index(24))  # 2, the first occurrence
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
# syntax
lst = ["item1", "item2"]
lst.sort()  # ascending
lst.sort(reverse=True)  # descending

fruits = ["banana", "orange", "mango", "lemon"]
fruits.sort()  # alphabetical sort
print(fruits)  # ['banana', 'lemon', 'mango', 'orange']

# alphabetical reverse sort
fruits.sort(reverse=True)  # ['orange', 'mango', 'lemon', 'banana']
print(fruits)

ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages)  # [19, 22, 24, 24, 24, 25, 25, 26]

ages.sort(reverse=True)
print(ages)  # [26, 25, 25, 24, 24, 24, 22, 19]


# sorted(): returns the ordered list without modifying the original list
print("\n--------- sorted()")
fruits = ["banana", "orange", "mango", "lemon"]
print(sorted(fruits))  # ['banana', 'lemon', 'mango', 'orange']

# Reverse order
fruits = ["banana", "orange", "mango", "lemon"]
fruits = sorted(fruits, reverse=True)
print(fruits)  # ['orange', 'mango', 'lemon', 'banana']
