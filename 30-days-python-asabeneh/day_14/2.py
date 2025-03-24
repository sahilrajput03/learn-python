print("------------------------ 1")


# * Mimicing decorator functionality via normal function:
def greeting():
    return "Welcome to Python"


def uppercase_decorator(function):
    def wrapper():
        return function().upper()

    return wrapper


g = uppercase_decorator(greeting)
print(g())  # WELCOME TO PYTHON

print("------------------------ 2")

## * Using decorators in python:
# This decorator function is a higher order function that takes a function as a parameter


def uppercase_decorator(function):
    def wrapper():
        return function().upper()

    return wrapper


@uppercase_decorator
def greeting():
    return "Welcome to Python"


print(greeting())  # WELCOME TO PYTHON
