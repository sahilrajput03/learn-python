"""These decorator functions are higher order functions
that take functions as parameters"""

# * Applying Multiple Decorators to a Single Function


# First Decorator
def uppercase_decorator(greetFn):
    print("1 - uppercase_decorator body")
    uppercaseFn = lambda: greetFn().upper()
    return uppercaseFn


# Second decorator
def split_string_decorator(uppercaseDecoratorFn):
    print("2 - split_string_decorator body")
    resultFn = lambda: uppercaseDecoratorFn().split()
    return resultFn


# & Learn: Notice the pattern that `greeting` function is passed as arugment to
# &     `uppercase_decorator` function. Then `uppercase_decorator` function is passed
# &     as an argument to `split_string_decorator` function.
@split_string_decorator  # * 2nd
@uppercase_decorator  # * 1st
def greeting():  # * 3rd
    print("3 - greetingFunction body")
    return "Welcome to Python"


print(greeting())  # WELCOME TO PYTHON
