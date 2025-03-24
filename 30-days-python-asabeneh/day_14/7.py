# * The filter() function calls the specified function which returns boolean for
#       each item of the specified iterable (list). it filters the items that satisfy
#       the filtering criteria.
# * SYNTAX
# filter(function, iterable)


print("--------------------------------- 1")
# Filter even numbers using `filter` function
numbers = [1, 2, 3, 4, 5]  # iterable
even_numbers = filter(lambda num: num % 2 == 0, numbers)
# print(even_numbers) # Prints address of the map object: <map object at 0x10ed60d30>
print(list(even_numbers))  # [2, 4]


print("\n\n--------------------------------- 2")

numbers = [1, 2, 3, 4, 5]  # iterable
odd_numbers = filter(lambda num: num % 2 != 0, numbers)
# print(odd_numbers) # Prints address of the map object: <map object at 0x10ed60d30>
print(list(odd_numbers))  # [1, 3, 5]


print("\n\n--------------------------------- 3")

# Filter long name
names = ["Asabeneh", "Lidiya", "Ermias", "Abraham"]  # iterable
long_names = filter(lambda name: len(name) > 7, names)
# print(long_names) # Prints address of the map object: <map object at 0x10ed60d30>
print(list(long_names))  # ['Asabeneh']
