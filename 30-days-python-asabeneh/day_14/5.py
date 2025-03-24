# * The map() function is a built-in higher order function that takes a function
# *     (i.e., first arugment) and iterates over items over the data (i.e, the
# *     second argument)
numberList = [1, 2, 3, 4, 5]  # iterable


def square(x):
    return x**2


numbers_squared = map(square, numberList)  # immutable function
# print(numbers_squared) # Prints address of the map object: <map object at 0x10ed60d30>
print(list(numbers_squared))  # [1, 4, 9, 16, 25]

# Passing lambda funtion as argument:
numbers_squared = map(lambda x: x**2, numberList)
# print(numbers_squared) # Prints address of the map object: <map object at 0x10ed60d30>
print(list(numbers_squared))  # [1, 4, 9, 16, 25]
