# * Python - Reduce Function
# * The reduce() function is defined in the functools module and we should
#   import it from this module. Like map and filter it takes two parameters, a
#   function and an iterable. However, it does not return another iterable,
#   instead it returns a single value. Example:1

from functools import reduce

print("---------- 1")
numbers_str = ["1", "2", "3", "4", "5"]  # iterable


def reduceFn(accumulator, current):
    print(accumulator, current)
    return int(accumulator) + int(current)


# * Without initial value
total = reduce(reduceFn, numbers_str)
print(total)  # 15

# * With initial value
print("\n\n---------- 2")
intialValue = 10
total = reduce(reduceFn, numbers_str, intialValue)
print(total)
