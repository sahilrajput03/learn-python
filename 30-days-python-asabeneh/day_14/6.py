print("--------------------------------- 1")
numbers_str = ["1", "2", "3", "4", "5"]  # iterable
numbers_int = map(int, numbers_str)
# print(numbers_int) # Prints address of the map object: <map object at 0x10ed60d30>
print(list(numbers_int))  # [1, 2, 3, 4, 5]

print("\n\n--------------------------------- 2")
names = ["Asabeneh", "Lidiya", "Ermias", "Abraham"]  # iterable


toUpper = lambda name: name.upper()
names_upper_cased = map(toUpper, names)
# print(names_upper_cased) # Prints address of the map object: <map object at 0x10ed60d30>
print(list(names_upper_cased))  # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']

# * Passing lambda function inline as argument:
names_upper_cased = map(lambda name: name.upper(), names)
# print(names_upper_cased) # Prints address of the map object: <map object at 0x10ed60d30>
print(list(names_upper_cased))  # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']
