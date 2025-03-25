# SyntaxError (can not be caught by try-catch)
# print "hello world"

# NameError
try:
    print(age)
except NameError:
    print("Got NameError because variable age is not defined")


# IndexError
numbers = [1, 2]
try:
    numbers[5]
except IndexError:
    print("Got IndexError because the index is out of range")


# ModuleNotFoundError
try:
    import maths  # an extra s to math deliberately to trigger error
except ModuleNotFoundError:
    print("Got ModuleNotFoundError because no module named maths")

import math

# AttributeError
try:
    math.PI  # Instead of `pi` we are intentionlly accessing `PI`
except AttributeError:
    print("Got AttributeError while executing math.PI")


# KeyError
user = {"name": "Asab", "age": 250, "country": "Finland"}
try:
    user["someNonExistingProperty"]
except KeyError:
    print("Got `KeyError` on running user[someNonExistingProperty].")

# TypeError
try:
    4 + "3"
except TypeError:
    print("Got TypeError while adding integer and string type variable.")

# ImportError
try:
    from math import power
except ImportError:
    print(
        "Got ImportError while importing non-existing function power from math module."
    )

# Learn: Correct way of usin `pow` function from math module:
from math import pow

pow(2, 3)  # 8.0

# ValueError
try:
    int("12a")
except ValueError:
    print("Got ValueError while running int('12a')")

# ZeroDivisionError
try:
    1 / 0
except ZeroDivisionError:
    print("Got ZeroDivisionError while running 1/0")
