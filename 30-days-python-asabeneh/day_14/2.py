print("------------------------ 1")


# * Mimicing decorator functionality via normal function:
greeting = lambda: "Welcome to Python"


def uppercase_decorator(greetFn):
    return lambda: greetFn().upper()


g = uppercase_decorator(greeting)
print(g())  # WELCOME TO PYTHON

print("------------------------ 2")

## * Using decorators in python:
# This decorator function is a higher order function that takes a function as a parameter


def uppercase_decorator(greetFn):
    return lambda: greetFn().upper()


# * Learn: The reason is that the decorator syntax @decorator can only be used with function definitions (using def), not with lambda expressions.
# & Learn: Notice the pattern that `greeting` function is passed as arugment to `uppercase_decorator` function.
@uppercase_decorator
def greeting():
    return "Welcome to Python"


print(greeting())  # WELCOME TO PYTHON
