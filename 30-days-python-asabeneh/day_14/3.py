"""These decorator functions are higher order functions
that take functions as parameters"""

# * Applying Multiple Decorators to a Single Function


# First Decorator
def uppercase_decorator(greetFn):
    print("1 - uppercase_decorator body")
    return lambda: greetFn().upper()


# Second decorator
def split_string_decorator(uppercaseFn):
    print("2 - split_string_decorator body")
    return lambda: uppercaseFn().split()


@split_string_decorator  # * 2nd
@uppercase_decorator  # * 1st
def greeting():  # * 3rd
    print("3 - greetingFunction body")
    return "Welcome to Python"


print(greeting())  # WELCOME TO PYTHON
