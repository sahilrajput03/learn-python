# Higher Order Functions
#  Python functions are treated as first class citizens, allowing you to perform
#       the following operations on functions:
# - A function can take one or more functions as parameters
# - A function can be returned as a result of another function
# - A function can be modified
# - A function can be assigned to a variable

# In this section, we will cover:
# - Handling functions as parameters
# - Returning functions as return value from another functions
# - Using Python closures and decorators

print("------------------------ 1")

# Function as a Parameter
sumFunction = lambda num: sum(num)  # Here `sum` is a builtin function.
higherOrderFunction = lambda f, lst: f(lst)  # function (`f`) as parameter
result = higherOrderFunction(sumFunction, [1, 2, 3, 4, 5])
print(result)  # 15


# ##############################################################
print("------------------------ 2")


def square(x):  # a square function
    return x**2


def cube(x):  # a cube function
    return x**3


def absolute(x):  # an absolute value function
    if x >= 0:
        return x
    else:
        return -(x)


def higher_order_function(type):  # a higher order function returning a function
    if type == "square":
        return square
    elif type == "cube":
        return cube
    elif type == "absolute":
        return absolute


# We can see from the below examples that the higher order function is returning different functions depending on the passed parameter
result = higher_order_function("square")
print("square:", result(3))  # 9
result = higher_order_function("cube")
print("cube:", result(3))  # 27
result = higher_order_function("absolute")
print("absolute:", result(-3))  # 3

print("------------------------ 3")

# PYTHON CLOSURES

# Python allows a nested function to access the outer scope of the enclosing
# function. This is is known as a Closure. Let us have a look at how closures
# work in Python. In Python, closure is created by nesting a function inside
# another encapsulating function and then returning the inner function. See the
# example below.


def add_ten():
    ten = 10

    def add(num):
        return num + ten

    return add


closure_result = add_ten()
print(closure_result(5))  # 15
print(closure_result(10))  # 20
