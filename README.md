_See older readme: [Click here](./README.old.md) (README.old.md)_

**Quick Links:**
- ❤️ 30 days of pythong: [Click here](https://github.com/Asabeneh/30-Days-Of-Python)
- ❤️ trekhleb/learn-python: [Click here](https://github.com/trekhleb/learn-python)


## What is `error`, `exception` and `exception handling` in python. Be concise. (ChatGPT)

Error: An issue in the program's syntax or logic that causes it to fail. Errors can be syntax errors (e.g., SyntaxError) or runtime errors (e.g., NameError, TypeError).

Exception: A type of runtime error that can be caught and handled using try-except blocks. Examples include ValueError, KeyError, and ZeroDivisionError.

*Errors terminate the program if unhandled, while exceptions allow for controlled recovery.*

**What is exception handling?**

Exception handling in Python refers to the process of managing and responding to runtime errors (exceptions) to prevent program crashes. It involves using constructs like `try`, `except`, `else`, and `finally` to handle exceptions gracefully.

Example:

```python
try:
    x = 10 / 0  # Potential exception
except ZeroDivisionError:
    print("Cannot divide by zero!")  # Handle the exception
else:
    print("No exceptions occurred.")  # Executes if no exceptions
finally:
    print("Execution complete.")  # Always executes
```

This ensures the program continues running even when unexpected issues arise.

# 30 Days of Python

Code generate via autodocs

## 😇😇😇 Todos:

- Continue doing day 5
    - [Content](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/05_Day_Lists/05_lists.md)
    - [Code](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/05_Day_Lists/day_5.py)
- (future todos to add here)

## File - `30-days-python-asabeneh/day_01/1.1.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_01/1.1.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_01/1.1.py -->
```py
# Day 1 - 30DaysOfPython Challenge

print(2 + 3)  #                                 addition(+)
print(3 - 1)  #                                 subtraction(-)
print(2 * 3)  #                                 multiplication(*)
print(3 / 2)  #                                 division(/)
print(3**2)  #                                  exponential(**)
print(3 % 2)  #                                 remainder/modulus(%)
print(3 // 2)  #                                Floor division operator(//)
print(1 + 3j)  #                                <class 'complex'>
print()

# Checking data types
print(type(10))  #                              <class 'int'>
print(type(3.14))  #                            <class 'float'>
print(type(1 + 3j))  #                          <class 'complex'>
print(type("Asabeneh"))  #                      <class 'str'>
print(type([1, 2, 3]))  #                       Li<class 'list'>st
print(type({"name": "Asabeneh"}))  #            <class 'dict'>
print(type({9.8, 3.14, 2.7}))  #                <class 'set'>
print(type((9.8, 3.14, 2.7)))  #                <class 'tuple'>
print()

a = b = 20
print(a, b)  # 20, 20
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_01/1.2.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_01/1.2.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_01/1.2.py -->
```py
# All below if statements resolve to true.

#### Using `type` function
if type(10) == int:
    print("integer type")

if type(3.14) == float:
    print("float type")

if type(1 + 3j) == complex:
    print("complex type")

if type("Asabeneh") == str:
    print("str type")

if type([1, 2, 3]) == list:
    print("list type")

if type({9.8, 3.14, 2.7}) == set:
    print("set type")

if type((9.8, 3.14, 2.7)) == tuple:
    print("tuple type")

if type(zip([1, 2], [3, 4])) == zip:
    print("zip type")


print()

#### However, it's often better to use isinstance() for type checking, as it
#     works with inheritance:

# check variable type using `isinstance`
if isinstance(10, int):
    print("integer type")

if isinstance(3.14, float):
    print("float type")

if isinstance(1 + 3j, complex):
    print("complex type")

if type("Asabeneh") == str:
    print("str type")

if isinstance([1, 2, 3], list):
    print("list type")

if isinstance({9.8, 3.14, 2.7}, set):
    print("set type")

if isinstance((9.8, 3.14, 2.7), tuple):
    print("tuple type")
if isinstance(zip([1, 2], [3, 4]), zip):
    print("zip type")
print()
```
<!-- MARKDOWN-AUTO-DOCS:END -->


## File - `30-days-python-asabeneh/day_01/2.1.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_01/2.1.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_01/2.1.py -->
```py
# Printing variables
# ##################

x = input("Please enter your name\n")
# x = 'Alice' # (Testing)

if type(x) == str:
    print("str type")

# f-strings (formatted string literals)     (Way 1)
print(
    f"{x}, good to meet you!"
)  # You can use single ('') or double ("") quotes as you wish
# Note:
# 1. From Python 3.6 (2016) we use this `f-strings` syntax widely for their
# readability and efficiency when formatting strings.)
# 2. This approach is concise and more efficient compared to older methods like
#    str.format() or string concatenation.


# Using str.format()                        (Way 2)
print(
    "{}, good to meet you!".format(x)
)  # You can use single ('') or double ("") quotes as you wish

# ####
# Note: Both methods (`f-strings` & `str.format`) allow you to include
# multiple variables in a string, but f-strings are generally preferred for
# their cleaner syntax. ###
# ####
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_01/2.2.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_01/2.2.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_01/2.2.py -->
```py
s = "sahil"
print(len(s))  # 5

if len(s) == 5:
    print("Yes it is a 5.")
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_01/2.3.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_01/2.3.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_01/2.3.py -->
```py
a = 4
b = 3
print(f"{a} + {b} = {a +b}")  #         4 + 3 = 7
print(f"{a} - {b} = {a - b}")  #        4 - 3 = 1
print(f"{a} * {b} = {a * b}")  #        4 * 3 = 12
print(f"{a} / {b} = {a / b:.2f}")  #    4 / 3 = 1.33
print(f"{a} % {b} = {a % b}")  #        4 % 3 = 1
print(f"{a} // {b} = {a // b}")  #      4 // 3 = 1
print(f"{a} ** {b} = {a ** b}")  #      4 ** 3 = 64
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_01/2.4.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_01/2.4.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_01/2.4.py -->
```py
simple = "Python"
a, b, c, d, e, f = simple  # unpacking sequence characters into variables
print(a)  # P
print(b)  # y
print(c)  # t
print(d)  # h
print(e)  # o
print(f)  # n
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_01/2.5.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_01/2.5.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_01/2.5.py -->
```py
language = "Python"

# extended slicing of a sequence (like a string, list, or tuple)
pto = language[0:6:2]
print(pto)  # "Pto"
print(type(pto) == str)  # True
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_01/3.1.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_01/3.1.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_01/3.1.py -->
```py
# Print weight in pounds, kg.
print("This is weight calculate machine...")


def toKg(pounds):
    return pounds / 2.2046


def toPounds(kg):
    return kg * 2.2046


def userInput():
    print("Q. Please choose pounds or kgs (p/k)...")
    choice = input("")
    if choice == "p":
        print("You choose pounds!!")
        pounds = int(input())
        print(toKg(pounds))

    elif choice == "k":
        print("You choose kgs")
        kg = int(input())
        print(toPounds(kg))
    else:
        print("You choose wrong, choose again!")
        userInput()


userInput()
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_01/3.2.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_01/3.2.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_01/3.2.py -->
```py
# Nested list comprehension example.
myLambda = lambda a, b, sum: a + b != sum  # Returns True or False

X = range(3)  # [0, 1, 2 , ...n-1]
Y = range(2)

# PRINTS ALL THE POINTS IN TWO-DIMENSION SPACE:
# * Learn: We can use the variable after `for` keyword in the expression at the front and that expression is returend as item in the list.
points = [[xval, yval] for xval in X for yval in Y]  # Prints all the points.
print(points)  # [[0, 0], [0, 1], [1, 0], [1, 1], [2, 0], [2, 1]]

# Note to Sahil: This above syntax of nested loop works like
# `for Loop1 for Loop2`
# Loop1 (e.g., X values in this case)
#       Loop2 (e.g, Y values in this case)


# Print values only when sum of values is `required_sum`
required_sum = 3

points = [
    [xval, yval] for xval in X for yval in Y if xval + yval != required_sum
]  # SIMPLE SOLUTION.
print(points)  # [[0, 0], [0, 1], [1, 0], [1, 1], [2, 0]]
# We learn in this example that we can pass a condition after the `for-loop` and return values if that condition passes.


points = [
    [xval, yval] for xval in X for yval in Y if myLambda(xval, yval, required_sum)
]  # SOLUTION USING LAMBDA FUNCTION.
print(points)  # [[0, 0], [0, 1], [1, 0], [1, 1], [2, 0]]
# We learn in this example that we can pass a lambda function after the `for-loop` and condition returned from
#   lambda function will judge whether to show a variable


# Sahil: Probably these ways are helpful in using when we need functionalities
# similar to `find` or `filter` array methods in Javascript.
```
<!-- MARKDOWN-AUTO-DOCS:END -->



## File - `30-days-python-asabeneh/day_01/3.3.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_01/3.3.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_01/3.3.py -->
```py
# Nested list comprehension example.
myLambda = lambda a, b, c, sum: a + b + c != sum  # Returns True or False

X = range(2)  # [0, 1, 2 , ...n-1]
Y = range(2)
Z = range(2)

# PRINTS ALL THE POINTS IN SPACE.
points = [
    [xval, yval, zval] for xval in X for yval in Y for zval in Z
]  # Prints all the points.
print(
    points
)  # [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]


# Print values only when sum of values is `required_sum`
required_sum = 2

points = [
    [xval, yval, zval]
    for xval in X
    for yval in Y
    for zval in Z
    if xval + yval + zval != required_sum
]  # SIMPLE SOLUTION.
print(points)  # [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
# We learn in this example that we can pass a condition after the `for-loop` and
# return values if that condition passes.

points = [
    [xval, yval, zval]
    for xval in X
    for yval in Y
    for zval in Z
    if myLambda(xval, yval, zval, required_sum)
]  # SOLUTION USING LAMBDA FUNCTION.
print(points)  # [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
# We learn in this example that we can pass a lambda function after the
#   `for-loop` and condition returned from lambda function will judge whether to
#   show a variable


# Sahil: Probably these ways are helpful in using when we need functionalities
# similar to `find` or `filter` array methods in Javascript.
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_01/4.1.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_01/4.1.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_01/4.1.py -->
```py
secret_number = 7  # right number

count = 1

allowed_attempts = 3


def game(count):
    i = int(
        input(
            f"You have {allowed_attempts} attempts to guess the number. \nTry your luck, choose a number:\n"
        )
    )
    count += 1
    if i == secret_number:
        print("Hooray..!")
    else:
        if count > allowed_attempts:
            print("Sorry, You loose!!")
            return  # terminate the function execution.
        game(count)


# Start the game
game(count)
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_01/5.1.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_01/5.1.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_01/5.1.py -->
```py
info = """
start - to start the car
stop - to stop the car
quit - to exit
"""

welcome_message = """🤠︎ Welcome to the game!"""

print(welcome_message, info)


def game(is_started):
    choice = input().lower()
    if choice == "help":
        print(info)
        game(is_started)
    elif choice == "start":
        if is_started == True:
            print("You car is already started🥶︎!")
            game(is_started)
        print("Your car started..🚀︎🚀︎!!.")
        is_started = True
        game(is_started)
    elif choice == "stop":
        if is_started == False:
            print("You car is already stopped🥶︎!")
            game(is_started)
        print("You car stopped ..🛑︎🛑︎")
        is_started = False
        game(is_started)
    elif choice == "quit":
        print("Thanks for playing the game 🧸︎")
        return
    else:
        print("I don't understand that...")
        print("Try again..")
        game(is_started)


game(False)

# Some case flow of this game:
"""
CASE: If user types any wrong choice..!
print >>> I don't understand that...

CASE: If choose start
Car started...Ready to go!

CASE: If choose stop
Car stopped.
"""
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_01/ex1.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_01/ex1.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_01/ex1.py -->
```py
point_a = [1, 1]
point_b = [3, 3]

# pseudo code
# d = (((y2-y1)**2 + (x2-x1)**2) )^(1/2)

distance = ((point_b[1] - point_a[1]) ** 2 + (point_b[0] - point_a[0]) ** 2) ** (1 / 2)
print("distance betwen two points:", distance)
```
<!-- MARKDOWN-AUTO-DOCS:END -->


## File - `30-days-python-asabeneh/day_02/1.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_02/1.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_02/1.py -->
```py
# bakchodi
text = "HelLOO"

# print all available methods on this value
print(dir(text))

print(text.upper())  # HELLOO
print(text.lower())  # helloo

print(text.startswith("Hel"))  # True
print(text.startswith("ABC"))  # False

person_info = {
    "firstname": "Asabeneh",
    "lastname": "Yetayeh",
    "country": "Finland",
    "city": "Helsinki",
}

print(person_info)
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_02/2.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_02/2.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_02/2.py -->
```py
first_name = input("What is your name: ")
age = input("How old are you? ")

print(first_name)
print(age)
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_02/3.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_02/3.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_02/3.py -->
```py
# int to float
num_int = 10
print("num_int", num_int)  # 10
num_float = float(num_int)
print("num_float:", num_float)  # 10.0

# float to int
gravity = 9.81
print(int(gravity))  # 9

# int to str
num_int = 10
print(num_int)  # 10
num_str = str(num_int)
print(num_str)  # '10'

# str to int or float
num_str = "10.6"
num_float = float(num_str)
print("num_float", float(num_str))  # 10.6
num_int = int(num_float)
print("num_int", int(num_int))  # 10

# str to list
first_name = "Asabeneh"
print(first_name)  # 'Asabeneh'
first_name_to_list = list(first_name)
print(first_name_to_list)  # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_02/ex1.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_02/ex1.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_02/ex1.py -->
```py
# num_one to the power of num_two
num_1 = 2
num_2 = 3

final_value = num_1**num_2
print(final_value)  # 8


# Find floor division of num_1 by num_2 and assign the value to a variable floor_division
final_value2 = num_2 // num_1
print(final_value2)  # 1
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_02/ex2.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_02/ex2.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_02/ex2.py -->
```py
# The radius of a circle is 30 meters.
# 1. Calculate the area of a circle and assign the value to a variable name of
# area_of_circle
# 2. Calculate the circumference of a circle and assign the value to a variable
# name of circum_of_circle Take radius as user input and calculate the area.

radius = input("Enter radius of circle: ")  # assuming input as 3
r = int(radius)
area_of_circle = 3.14 * r**2
print(area_of_circle)  # 28.26


circum_of_circle = 2 * 3.14 * r
print(circum_of_circle)  # 18.84
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_02/ex3.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_02/ex3.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_02/ex3.py -->
```py
help("keywords")
# Output
"""
Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not    
"""
```
<!-- MARKDOWN-AUTO-DOCS:END -->


## File - `30-days-python-asabeneh/day_03/1.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_03/1.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_03/1.py -->
```py
# source of this file:
# https://github.com/Asabeneh/30-Days-Of-Python/blob/master/03_Day_Operators/day-3.py
# Note to Sahil: I have kept only non-repetitive code in this file from above
# reference file.

print("Multiplying complex number: ", (1 + 1j) * (1 - 1j))

print(3 > 2)  # True, because 3 is greater than 2
print(3 >= 2)  # True, because 3 is greater than 2
print(3 < 2)  # False,  because 3 is greater than 2
print(2 < 3)  # True, because 2 is less than 3
print(2 <= 3)  # True, because 2 is less than 3
print(3 == 2)  # False, because 3 is not equal to 2
print(3 != 2)  # True, because 3 is not equal to 2
print(len("mango") == len("avocado"))  # False
print(len("mango") != len("avocado"))  # True
print(len("mango") < len("avocado"))  # True
print(len("milk") != len("meat"))  # False
print(len("milk") == len("meat"))  # True
print(len("tomato") == len("potato"))  # True
print(len("python") > len("dragon"))  # False

# Boolean comparison
print("True == True: ", True == True)  # True
print("True == False: ", True == False)  # False
print("False == False:", False == False)  # True
print("True and True: ", True and True)  # True
print("True or False:", True or False)  # True


# Another way comparison
# ======================
# print("1 is 1", 1 is 1)  # True - because the data values are the same
# print("1 is not 2", 1 is not 2)  # True - because 1 is not 2
# print("4 is 2 ** 2:", 4 is 2**2)  # True
"""
* Sahil: Above three statements throws syntax warning because it isn't recommended approach.
* We get this warning -
`SyntaxWarning: "is" with a literal. Did you mean "=="?`

The is operator should primarily be used for:
1. Comparing with None
2 Identity comparison when you specifically need to check if two variables reference the same object
"""

print("A in Asabeneh", "A" in "Asabeneh")  # True - A found in the string
print("B in Asabeneh", "B" in "Asabeneh")  # False -there is no uppercase B
print("coding" in "coding for all")  # True - because coding for all has the word coding
print("coding" not in "coding for all")  # False
print("xyz" not in "coding for all")  # True
print("a in an:", "a" in "an")  # True
print(3 > 2 and 4 > 3)  # True - because both statements are true
print(3 > 2 and 4 < 3)  # False - because the second statement is false
print(3 < 2 and 4 < 3)  # False - because both statements are false
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statement is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print(not 3 > 2)  # False - because 3 > 2 is true, then not True gives False
print(not True)  # False - Negation, the not operator turns true to false
print(not False)  # True
print(not not True)  # True
print(not not False)  # False
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_03/ex1.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_03/ex1.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_03/ex1.py -->
```py
# Write a script that prompts the user to enter side a, side b, and side c of
# the triangle.
#  - Calculate the perimeter of the triangle (perimeter = a + b + c).
a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))

print(f"The perimeter of the triangle is {a+b+c}")  # The perimeter of the triangle is 9
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_03/ex2.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_03/ex2.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_03/ex2.py -->
```py
# Find the length of the text python and convert the value to float and convert
# it to string
a = len("python")
print(a)  # 6

b = float(a)
print(b)  # 6.0

c = str(b)
print(c)
print(type(c))  # <class 'str'>
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_03/ex3.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_03/ex3.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_03/ex3.py -->
```py
# Check if type of '10' is equal to type of 10
a = "10"
b = 10
print(type(a) == type(b))  # False

try:
    # Check if int('9.8') is equal to 10
    # This statement throws runtime error: `ValueError: invalid literal for
    # int() with base 10: '9.8'``
    c = int("9.8")
except ValueError:
    print("Got ValueError")  # Got ValueError
else:
    print("No exceptions occurred.")
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_03/ex4.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_03/ex4.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_03/ex4.py -->
```py
# Write a script that prompts the user to enter number of years. Calculate the
# number of seconds a person can live. Assume a person can live hundred years
# SAMPLE:
#   Enter number of years you have lived: 100
#   You have lived for 3153600000 seconds.


years = int(input("Enter number of years you have lived: "))  # assuming input 100
seconds = years * 365 * 24 * 60 * 60
print(f"You have lived for {seconds} seconds.")

print(3153600000 == seconds)  # True (assuming we entered `years = 100`)
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_03/ex5.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_03/ex5.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_03/ex5.py -->
```py
# Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125

a = 1
b = 1
d = 1
e = 1

print(f"{a} {b} {a} {a**2} {a**3}")
a = a + 1

print(f"{a} {b} {a} {a**2} {a**3}")
a = a + 1

print(f"{a} {b} {a} {a**2} {a**3}")
a = a + 1

print(f"{a} {b} {a} {a**2} {a**3}")
a = a + 1

print(f"{a} {b} {a} {a**2} {a**3}")
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_04/1.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_04/1.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_04/1.py -->
```py
# source of this and following files in this day --
# https://github.com/Asabeneh/30-Days-Of-Python/blob/master/04_Day_Strings/day_4.py

# Single line comment
letter = "P"  # A string could be a single character or a bunch of texts
print(letter)  # P
print(len(letter))  # 1

greeting = "Hello, World!"  # String could be  a single or double quote,"Hello, World!"
print(greeting)  # Hello, World!
print(len(greeting))  # 13

sentence = "I hope you are enjoying 30 days of python challenge"
print(sentence)
print()

# Multiline String
multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)
print()

# Another way of doing the same thing
multiline_string = "I am a teacher and enjoy teaching.\nI didn't find anything as rewarding as empowering people.\nThat is why I created 30 days of python."
print(multiline_string)
print()


lines = [
    "I am a teacher and enjoy teaching.",
    "I didn't find anything as rewarding as empowering people.",
    "That is why I created 30 days of python.",
]
"\n".join(lines)
print(lines)
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_04/2.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_04/2.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_04/2.py -->
```py
# String Concatenation
first_name = "Asabeneh"
last_name = "Yetayeh"
space = " "
full_name = first_name + space + last_name
print(full_name)  # Asabeneh Yetayeh
print()

#### Unpacking characters
language = "Python"
a, b, c, d, e, f = language  # unpacking sequence characters into variables
print(a)  # P
print(b)  # y
print(c)  # t
print(d)  # h
print(e)  # o
print(f)  # n
print()

# Accessing characters in strings by index
language = "Python"
print(language[0])  # P
print(language[1])  # y
last_letter = language[len(language) - 1]
print(last_letter)  # n
print()

# If we want to start from right end we can use negative indexing. -1 is the last index
language = "Python"
# get last letter
print(language[-1])  # n
# get second last letter
print(language[-2])  # o
print()


# Slicing
language = "Python"
first_three = language[0:3]  # starts at zero index and up to 3 but not include 3
print(first_three)

last_three = language[3:6]
print(last_three)  # hon
# Another way
last_three = language[-3:]
print(last_three)  # hon
last_three = language[3:]
print(last_three)  # hon
print()

# Reversing a String: We can easily reverse strings in python.
greeting = "Hello, World!"
print(greeting[::-1])  # !dlroW ,olleH


# Skipping character while splitting Python strings
language = "Python"
pto = language[0:6:2]  #
"""
Python's slice notation with three parameters: [start:end:step]
Let's break it down:
0 is the starting index
6 is the ending index (exclusive)
2 is the step (or stride) - meaning it takes every 2nd character
"""
print(pto)  # Pto
print()


"""
Escape Sequences in Strings
In Python and other programming languages \ followed by a character is an escape
sequence. Let us see the most common escape characters:

\n: new line \t: Tab means(8 spaces) \\: Back slash \': Single quote (') \":
Double quote (")
"""
print("I hope every one enjoying the python challenge.\nDo you ?")  # line break
# Output
"""
I hope every one enjoying the python challenge.
Do you ?
"""

print("Days\tTopics\tExercises")
print("Day 1\t3\t5")
print("Day 2\t3\t5")
print("Day 3\t3\t5")
print("Day 4\t3\t5")
print("This is a back slash  symbol (\\)")  # To write a back slash
print('In every programming language it starts with "Hello, World!"')
# Output
"""
Days	Topics	Exercises
Day 1	3	5
Day 2	3	5
Day 3	3	5
Day 4	3	5
This is a back slash  symbol (\)
In every programming language it starts with "Hello, World!"
"""
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_04/3.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_04/3.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_04/3.py -->
```py
## String Methods
# capitalize(): Converts the first character the string to Capital Letter
challenge = "thirty days of python"
print(challenge.capitalize())  # 'Thirty days of python'

# count(): returns occurrences of substring in string, count(substring, start=.., end=..)
challenge = "thirty days of python"
print(challenge.count("y"))  # 3
print(challenge.count("y", 7, 14))  # 1
print(challenge.count("th"))  # 2`

# endswith(): Checks if a string ends with a specified ending
challenge = "thirty days of python"
print(challenge.endswith("on"))  # True
print(challenge.endswith("tion"))  # False

# expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument
# By default the \t expands to 8 spaces
challenge = "thirty\tdays\tof\tpython"
print(challenge)
print(challenge.expandtabs())  # 'thirty  days    of      python'
# We can pass how many spaces to use for tabs by passing argument
print(challenge.expandtabs(10))  # 'thirty    days      of        python'

# find(): Returns the index of first occurrence of substring
challenge = "thirty days of python"
print(challenge.find("y"))  # 5
print(challenge.find("th"))  # 0
print()


# rfind(): Returns the index of the last occurrence of a substring, if not found returns -1
challenge = "thirty days of python"
print(challenge.rfind("y"))  # 16
print(challenge.rfind("th"))  # 17


# isalnum(): Checks alphanumeric character
challenge = "ThirtyDaysPython"
print(challenge.isalnum())  # True

challenge = "30DaysPython"
print(challenge.isalnum())  # True

challenge = "thirty days of python"
print(challenge.isalnum())  # False

challenge = "thirty days of python 2019"
print(challenge.isalnum())  # False

# isalpha(): Checks if all characters are alphabet characters (a-z and A-Z)
challenge = "thirty days of python"
print(challenge.isalpha())  # True
num = "123"
print(num.isalpha())  # False
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_04/4.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_04/4.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_04/4.py -->
```py
# isdigit(): Checks if all characters in a string are numbers (0-9 and some
# other unicode characters for numbers)
print("Thirty".isdigit())  # False
print("30".isdigit())  # True
print("\u00B2")  # ²
print("\u00B2".isdigit())  # True
print()

# isdecimal(): Checks if all characters in a string are decimal (0-9)
print("isdecimal()")
print("10".isdecimal())  # True
print("10.5".isdecimal())  # False
print("thirty days of python".isdecimal())  # False
print("123".isdecimal())  # True
print("12 3".isdecimal())  # False, space not allowed
print()


# isidentifier():Checks for valid identifier means it check if a string is a
# valid variable name
challenge = "30DaysOfPython"
print(challenge.isidentifier())  # False, because it starts with a number
challenge = "thirty_days_of_python"
print(challenge.isidentifier())  # True


# islower():Checks if all alphabets in a string are lowercase
challenge = "thirty days of python"
print(challenge.islower())  # True
challenge = "Thirty days of python"
print(challenge.islower())  # False

# isupper(): returns if all characters are uppercase characters
challenge = "thirty days of python"
print(challenge.isupper())  #  False
challenge = "THIRTY DAYS OF PYTHON"
print(challenge.isupper())  # True
print()


# isnumeric():Checks numeric characters
print("isnumeric()")
num = "10"
print(num.isnumeric())  # True
print("ten".isnumeric())  # False
num = "\u00BD"  # ½
print(num)
print(num.isnumeric())  # True
num = "10.5"
print(num.isnumeric())  # False
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_04/5.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_04/5.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_04/5.py -->
```py
# join(): Returns a concatenated string
web_tech = ["HTML", "CSS", "JavaScript", "React"]
result = ", ".join(web_tech)
print(result)  # 'HTML, CSS, JavaScript, React'
print()


# strip(): Removes all given characters starting from the beginning and end of the string
print("strip()")
print(" Thirty days of python ")
# Removes leading and trailing white space character
print(" Thirty days of python ".strip())
print("thirty days of pythonBATMAN".strip("BATMAN"))  # "thirty days of python"
print()


# replace(): Replaces substring inside
challenge = "thirty days of python"
print(challenge.replace("python", "coding"))  # 'thirty days of coding'

# split():Splits String from Left
challenge = "thirty days of python"
print(challenge.split())  # ['thirty', 'days', 'of', 'python']
challenge = "thirty, days, of, python"
print(challenge.split(", "))  # ['thirty', 'days', 'of', 'python']

# title(): Returns a Title Cased String
challenge = "thirty days of python"
print(challenge.title())  # Thirty Days Of Python
print()

# swapcase(): Checks if String Starts with the Specified String
"""
The swapcase() method returns a new string where all the case swapping rules below are applied:

Uppercase characters are converted to lowercase
Lowercase characters are converted to uppercase
All other characters remain unchanged
"""
challenge = "thirty days of python"
print(challenge.swapcase())  # THIRTY DAYS OF PYTHON
challenge = "Thirty Days Of Python"
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON

# startswith(): Checks if String Starts with the Specified String
challenge = "thirty days of python"
print(challenge.startswith("thirty"))  # True
challenge = "30 days of python"
print(challenge.startswith("thirty"))  # False
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_04/6.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_04/6.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_04/6.py -->
```py
"""
😇😇😇 String formatting
Old Style String Formatting (% Operator)
In Python there are many ways of formatting strings. In this section, we will
    cover some of them. The "%" operator is used to format a set of variables
    enclosed in a "tuple" (a fixed size list), together with a format string, which
    contains normal text together with "argument specifiers", special symbols like
    "%s", "%d", "%f", "%.number of digitsf".

%s - String (or any object with a string representation, like numbers)
%d - Integers
%f - Floating point numbers
"%.number of digitsf" - Floating point numbers with fixed precision
"""

# Strings only
first_name = "Asabeneh"
last_name = "Yetayeh"
language = "Python"
formated_string = "I am %s %s. I teach %s" % (first_name, last_name, language)
print(formated_string)

# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius**2
formated_string = "The area of circle with a radius %d is %.2f." % (
    radius,
    area,
)  # 2 refers the 2 significant digits after the point

python_libraries = ["Django", "Flask", "NumPy", "Matplotlib", "Pandas"]
formated_string = "The following are python libraries:%s" % (python_libraries)
print(formated_string)
# Output: "The following are python libraries:['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']"

"""
😇😇😇 New Style String Formatting (str.format)
This formatting is introduced in Python version 3.
"""
first_name = "Asabeneh"
last_name = "Yetayeh"
language = "Python"
formated_string = "I am {} {}. I teach {}".format(first_name, last_name, language)
print(formated_string)
a = 4
b = 3

radius = 10
pi = 3.14
area = pi  # radius ## 2
result = "The area of circle with {} is {}".format(str(radius), str(area))
print(result)  # The area of circle with 10 is 314.0
result = "The area of circle with {} is {}".format(radius, area)
print(result)  # The area of circle with 10 is 314.0


print("{} + {} = {}".format(a, b, a + b))  # 4 + 3 = 7
print("{} - {} = {}".format(a, b, a - b))  # 4 - 3 = 1
print("{} * {} = {}".format(a, b, a * b))  # 4 * 3 = 12
print("{} / {} = {:.2f}".format(a, b, a / b))  # limits it to two digits after decimal
# Output: 4 / 3 = 1.33

print("{} % {} = {}".format(a, b, a % b))  # 4 % 3 = 1
print("{} // {} = {}".format(a, b, a // b))  # 4 // 3 = 1
print("{} ** {} = {}".format(a, b, a**b))  # 4 ** 3 = 64


# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius**2
formated_string = "The area of a circle with a radius {} is {:.2f}.".format(
    radius, area
)  # 2 digits after decimal
print(formated_string)


"""
😇😇😇 String Interpolation / f-Strings (Python 3.6+) (Release date: Dec, 2016)
Another new string formatting is string interpolation, f-strings. Strings start
with f and we can inject the data in their corresponding positions.
"""
a = 4
b = 3
print(f"{a} + {b} = {a +b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")
```
<!-- MARKDOWN-AUTO-DOCS:END -->


## File - `30-days-python-asabeneh/day_04/7.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_04/7.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_04/7.py -->
```py
# index(): Returns the lowest index of a substring, additional arguments
# indicate starting and ending index (default 0 and string length - 1). If the
# substring is not found it raises a valueError.
challenge = "thirty days of python"
sub_string = "da"
print(challenge.index(sub_string))  # 7

try:
    # This statement throws runtime error: `ValueError: invalid literal for int() with base 10: '9.8'``
    print(challenge.index(sub_string, 9))
except ValueError:
    print("Got ValueError")  # Got ValueError
else:
    print("No exceptions occurred.")


# rindex(): Returns the highest index of a substring, additional arguments
# indicate starting and ending index (default 0 and string length - 1)
challenge = "thirty days of python"
sub_string = "da"
print(challenge.rindex(sub_string))  # 7
print(challenge.rindex("on", 8))  # 19


try:
    # This statement throws runtime error: `ValueError: invalid literal for
    # int() with base 10: '9.8'``
    print(challenge.rindex(sub_string, 9))
except ValueError:
    print("Got ValueError")  # Got ValueError
else:
    print("No exceptions occurred.")
```
<!-- MARKDOWN-AUTO-DOCS:END -->


## File - `30-days-python-asabeneh/day_04/ex1.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_04/ex1.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_04/ex1.py -->
```py
# 9. Cut(slice) out the first word of 'Coding For All' string.
string = "Coding For All"
print(string.split(" ")[0])

"""
10. Check if "Coding For All" string contains a word "Coding" using the method:
- index
- find or other methods.
"""
word = "Coding"

try:
    # Note: If `word` is not found in `string below statement throws runtime error (`ValueError: substring not found`)
    indexOfWord = string.index(word)
except ValueError:
    print("Got ValueError")
else:
    print("No exceptions occurred.")  # "No exceptions occurred."


print(type(indexOfWord) == int)  # True


indexOfWord = string.find(word) != -1
print(indexOfWord)  # True

# 18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
string1 = "Python For Everyone"
list = string1.split()
acronym = list[0][0] + list[1][0] + list[2][0]
print(acronym)
```
<!-- MARKDOWN-AUTO-DOCS:END -->

# Day 5

- Lists

There are four collection data types in Python :

1. List: is a collection which is ordered and changeable(modifiable). Allows duplicate members.
2. Tuple: is a collection which is ordered and unchangeable or unmodifiable(immutable). Allows duplicate members.
3. Set: is a collection which is unordered, un-indexed and unmodifiable, but we can add new items to the set. Duplicate members are not allowed.
4. Dictionary: is a collection which is unordered, changeable(modifiable) and indexed. No duplicate members.

- A list is collection of different data types which is ordered and modifiable(mutable). A list can be empty or it may have different data type items.


## File - `30-days-python-asabeneh/day_05/1.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_05/1.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_05/1.py -->
```py
# source -
# https://github.com/Asabeneh/30-Days-Of-Python/blob/master/05_Day_Lists/day_5.py

empty_list = list()  # this is an empty list, no item in the list
print(len(empty_list))  # 0
print(len(empty_list) == 0)  # True

# Lists can have items of different data types
lst = [
    "Asabeneh",
    250,
    True,
    {"country": "Finland", "city": "Helsinki"},
]

# sq bracket syntax
fruits = ["banana", "orange", "mango", "lemon"]  # list of fruits
print(fruits)  #  ['banana', 'orange', 'mango', 'lemon']
print(len(fruits))  # 4
print(fruits[0])  # banana
print(fruits[1])  # orange
print(fruits[len(fruits) - 1])  # lemon
print(fruits[-2])  # mango (accessing second last item)
print("-----")

# --- Unpacking List Items - example 1  ---
lst = ["item1", "item2", "item3", "item4", "item5"]
first_item, second_item, third_item, *rest = lst
print(first_item)  # item1
print(second_item)  # item2
print(third_item)  # item3
print(rest)  # ['item4', 'item5']
print("-----")

# Unpacking List Items - example 2
first, second, third, *rest, tenth = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(first)  # 1
print(second)  # 2
print(third)  # 3
print(rest)  # [4,5,6,7,8,9]
print(tenth)  # 10

# ---- Slicing items ----
# Positive Indexing: We can specify a range of positive
# indexes by specifying the start, end and step, the return value will be a new
# list.
# 🚀 Default Arguments:
# 1. startIndex = 0 (inclusive)
# 2. endIndex = len(lst) (exclusive)
# 3. step = 1
fruits = ["banana", "orange", "mango", "lemon"]
print(fruits[0:4])  # returns all the fruits

#  If we don't specify endIndex then default value is used i.e, `len(lst)`
print(fruits[0:])  # returns all the fruits as above

# start items including item at index 1 and exclude item at index 3
print(fruits[1:3])  # ['orange', 'mango']
print(fruits[1:])  # ['orange', 'mango', 'lemon']
print("------")
print("------")

fruits = ["banana", "orange", "mango", "lemon"]
# negative indexes works like this:
#  "banana"   "orange"   "mango"   "lemon"
#      0          1          2         3
#     -4         -3         -2        -1

print(fruits[-4:])  # ["banana", "orange", "mango", "lemon"]
print(fruits[-3:-1])  # ['orange', 'mango']         # does not include the end index
print(fruits[-3:])  # ['orange', 'mango', 'lemon']


print("------ STEP EXAMPLE")
# here we used a 3rd argument, step. It will take every 2nd item - ['banana', 'mango']
fruits = ["banana", "orange", "mango", "lemon"]
print(fruits[::2])  # ['banana', 'mango']


print("------ NEGATIVE STEP EXAMPLE")
# a negative step will take the list in reverse order
print(fruits[::-1])  # ['lemon', 'mango', 'orange', 'banana']


print("\n------ Modifying List")
fruits = ["banana", "orange", "mango", "lemon"]
fruits[0] = "Avocado"
print(fruits)  #  ['avocado', 'orange', 'mango', 'lemon']

fruits[1] = "apple"
print(fruits)  #  ['avocado', 'apple', 'mango', 'lemon']

fruits[len(fruits) - 1] = "lime"
print(fruits)  #  ['avocado', 'apple', 'mango', 'lime']
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_05/2.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_05/2.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_05/2.py -->
```py
# checking items: Checking an item if it is a member of a list using in operator
fruits = ["banana", "orange", "mango", "lemon"]
print("banana" in fruits)  # True
print("lime" in fruits)  # False

print("--------- append(): To add item in the end of the list")
fruits = ["banana", "orange", "mango", "lemon"]
fruits.append("apple")
print(fruits)  # ['banana', 'orange', 'mango', 'lemon', 'apple']
fruits.append("lime")  # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime]
print(fruits)

print("\n--------- insert(): To add/put item at specified index")
fruits = ["banana", "orange", "mango", "lemon"]
# * Learn: insert() function expected 2 arguments else we get error - `TypeError: insert expected 2 arguments, got 1`
fruits.insert(2, "apple")  # insert apple between orange and mango
print(fruits)  # ['banana', 'orange', 'apple', 'mango', 'lemon']
fruits.insert(3, "lime")
print(fruits)  # ['banana', 'orange', 'apple', 'lime', 'mango','lemon']

print("\n--------- .remove(itemHere): Removing specified item from list")
fruits = ["banana", "orange", "mango", "lemon"]
fruits.remove("banana")
print(fruits)  # ['orange', 'mango', 'lemon']
fruits.remove("lemon")
print(fruits)  # ['orange', 'mango']

# .pop(): Remove last item (when no argument is specified) OR remove item at specified index
fruits = ["banana", "orange", "mango", "lemon"]
fruits.pop()
print(fruits)  # ['banana', 'orange', 'mango']

fruits.pop(0)  # remove item at index 0
print(fruits)  # ['orange', 'mango']

# del
print("\n--------- del")
fruits = ["banana", "orange", "mango", "lemon"]
del fruits[0]
print(fruits)  # ['orange', 'mango', 'lemon']
print("---------")

del fruits[1]
print(fruits)  # ['orange', 'lemon']

print("--------- DELETE THE ITEMS IN THE RANGE YOU SPECIFY")
fruits = ["banana", "orange", "mango", "lemon"]
# Deletes items between given indexes, so it does not delete the item with index 3!
del fruits[1:3]
print(fruits)  # ['banana', 'lemon']


del fruits  # to delete the list completely
# print(fruits)  # Throws: NameError: name 'fruits' is not defined

print("\n--------- clear")
fruits = ["banana", "orange", "mango", "lemon"]
fruits.clear()
print(fruits)  # []
print("---------")

# copying a list
fruits = ["banana", "orange", "mango", "lemon"]
fruits_copy = fruits.copy()
fruits_copy.append("apple")
print(fruits)  # ['banana', 'orange', 'mango', 'lemon']
print(fruits_copy)  # ['banana', 'orange', 'mango', 'lemon', 'apple']
print("---------")
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_05/3.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_05/3.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_05/3.py -->
```py
# join - example 1
positive_numbers = [1, 2, 3]
zero = [0]
negative_numbers = [-3, -2, -1]
integers = negative_numbers + zero + positive_numbers
print(integers)  # [-3, -2, -1, 0, 1, 2, 3]
print("---------")


# join - example 2
fruits = ["banana", "orange", "mango", "lemon"]
vegetables = ["Tomato", "Potato", "Cabbage", "Onion", "Carrot"]
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)


# join with extend - `list1.extend(list2)`
num1 = [0, 1, 2, 3]
num2 = [4, 5, 6]
num1.extend(num2)
print(num1)  #  [0, 1, 2, 3, 4, 5, 6]
print("---------")


# .count() : To count the number of given items in the list
fruits = ["banana", "orange", "mango", "lemon"]
print(fruits.count("orange"))  # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))  # 3
print("---------")

# .index(): To get the index of specified item
fruits = ["banana", "orange", "mango", "lemon"]
print(fruits.index("orange"))  # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))  # 2, the first occurrence
print("---------")


# Reverse - example 1
fruits = ["banana", "orange", "mango", "lemon"]
fruits.reverse()
print(fruits)  # ['lemon', 'mango', 'orange', 'banana']

# Reverse - example 2
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages)  # [24, 25, 24, 26, 25, 24, 19, 22]


# .sort(): To sort the items in ascending order. You can specify `reverse=True` to get in descending order.
# syntax
lst = ["item1", "item2"]
lst.sort()  # ascending
lst.sort(reverse=True)  # descending

fruits = ["banana", "orange", "mango", "lemon"]
fruits.sort()  # alphabetical sort
print(fruits)  # ['banana', 'lemon', 'mango', 'orange']

# alphabetical reverse sort
fruits.sort(reverse=True)  # ['orange', 'mango', 'lemon', 'banana']
print(fruits)

ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages)  # [19, 22, 24, 24, 24, 25, 25, 26]

ages.sort(reverse=True)
print(ages)  # [26, 25, 25, 24, 24, 24, 22, 19]


# sorted(): returns the ordered list without modifying the original list
print("\n--------- sorted()")
fruits = ["banana", "orange", "mango", "lemon"]
print(sorted(fruits))  # ['banana', 'lemon', 'mango', 'orange']

# Reverse order
fruits = ["banana", "orange", "mango", "lemon"]
fruits = sorted(fruits, reverse=True)
print(fruits)  # ['orange', 'mango', 'lemon', 'banana']
```
<!-- MARKDOWN-AUTO-DOCS:END -->

# 🛑🛑🛑🛑Todo: continue doing exercise of day 5🛑🛑🛑🛑

[https://github.com/Asabeneh/30-Days-Of-Python/blob/master/05_Day_Lists/05_lists.md#-exercises-day-5](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/05_Day_Lists/05_lists.md#-exercises-day-5)


## File - `30-days-python-asabeneh/day_13/1.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_13/1.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_13/1.py -->
```py
# List comprehension in Python is a compact way of creating a list from a sequence
# *syntax*
# [i for i in iterable if expression]

# (Sahil) Learn: List comprehension in python is anonymous to a combination of both `map` and `filter` method of javascript.

# * Converting string to list comprehension
# * 1st Way
language = "Python"
lst = list(language)  # changing the string to list
print(type(lst))  # list
print(lst)  # ['P', 'y', 't', 'h', 'o', 'n']

# * 2nd Way
lst = [i for i in language]
print(type(lst))  # list
print(lst)  # ['P', 'y', 't', 'h', 'o', 'n']


# Learn: Range is not a primitive data type but a "class"
print(type(range(11)))  # "range" type
if isinstance(range(11), range):
    print("range type")

# #################
# Generating numbers
numbers = [i for i in range(11)]  # to generate numbers from 0 to 10
print(numbers)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# It is possible to do mathematical operations during iteration
squares = [i * i for i in range(11)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Learn: From Sahil: This is like map in javascript. This way we create tuples form a list:
numbers = [(i, i * i) for i in range(11)]
print(numbers)  # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_13/2.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_13/2.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_13/2.py -->
```py
# Generating even numbers in range 0 to 21
even_numbers = [
    i  # Here `i` is from last line
    for i in range(21)
    if i % 2 == 0  # Here `i` is from above line
]
print(even_numbers)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Generating odd numbers in range 0 to 21
odd_numbers = [
    i  # Here `i` is from last line
    for i in range(21)
    if i % 2 != 0  # Here `i` is from above line
]
print(odd_numbers)  # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Filter (getting) +ve even numbers from a `list` variable
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [
    i  # Here `i` is from last line
    for i in numbers
    if i % 2 == 0 and i > 0  # Here `i` is from above line
]
print(positive_even_numbers)  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Flattening a three dimensional list/array
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [
    item  # Here `item` variable is from last line
    for list in list_of_lists
    for item in list  # Here `list` variable is from above line
]
print(flattened_list)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_13/3.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_13/3.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_13/3.py -->
```py
# Lambda function Synatx
# x = lambda param1, param2, param3: param1 + param2 + param2
# print(x(arg1, arg2, arg3))


# Named function
def sum1(a, b):
    return a + b


print(sum1(2, 3))  # 5

# Using lambda function
sum2 = lambda a, b: a + b
print(sum2(2, 3))  # 5

# Self invoking lambda function (Immediately Invoked Lambda Function) ~ Sahil
print((lambda a, b: a + b)(100, 102))  # 202

square = lambda x: x**2
print(square(3))  # 9

cube = lambda x: x**3
print(cube(3))  # 27

# Multiple variables
y = lambda a, b, c: a**2 - 3 * b + 4 * c
print(y(5, 5, 3))  # 22
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_13/4.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_13/4.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_13/4.py -->
```py
# Lambda Function Inside Another Function
def power(x):
    return lambda n: x**n


# Learn: Here `2` is `x` and `3` is `n` thus --- 2**3 = 8
print(power(2)(3))  # 8

# Learn: Here `2` is `x` and `5` is `n` thus --- 2**5 = 32
print(power(2)(5))  # 32
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_13/ex1.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_13/ex1.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_13/ex1.py -->
```py
# Ex1: Filter only negative and zero in the list using list comprehension
list1 = [-4, -3, -2, -1, 0, 2, 4, 6]
print([i for i in list1 if i <= 0])
# Output: [-4, -3, -2, -1, 0]
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_13/ex2.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_13/ex2.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_13/ex2.py -->
```py
# Ex2: Flatten the following list of lists of lists to a one dimensional list :
y = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
# Expected output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

list = [
    item  # Here `item` is from last line
    for nestedList in y
    for subNestedList in nestedList  # Here `nestedList` is from above line
    for item in subNestedList  # Here `subNestedList` is from above line
]
print(list)
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_13/ex3.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_13/ex3.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_13/ex3.py -->
```py
# Ex3: Using list comprehension create the following list of tuples:
[
    (0, 1, 0, 0, 0, 0, 0),
    (1, 1, 1, 1, 1, 1, 1),
    (2, 1, 2, 4, 8, 16, 32),
    (3, 1, 3, 9, 27, 81, 243),
    (4, 1, 4, 16, 64, 256, 1024),
    (5, 1, 5, 25, 125, 625, 3125),
    (6, 1, 6, 36, 216, 1296, 7776),
    (7, 1, 7, 49, 343, 2401, 16807),
    (8, 1, 8, 64, 512, 4096, 32768),
    (9, 1, 9, 81, 729, 6561, 59049),
    (10, 1, 10, 100, 1000, 10000, 100000),
]


list = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(0, 11)]

# We are on purpose printing each item in new line to easily compare the expected output:
for item in list:
    print(item)
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_13/ex4.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_13/ex4.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_13/ex4.py -->
```py
# Ex4: Flatten the following list to a new list:
countries = [[("Finland", "Helsinki")], [("Sweden", "Stockholm")], [("Norway", "Oslo")]]

# output:
# [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]

list = [
    [country.upper(), country[:3].upper(), capital.upper()]
    # In above line `country` and `capital` is from last line
    for list in countries
    for (country, capital) in list  # Here `list` is from above line
    # In above line we are destructuring tuple values
]
print(list)
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_13/ex5.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_13/ex5.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_13/ex5.py -->
```py
# Ex5: Change the following list to a list of dictionaries:
countries = [[("Finland", "Helsinki")], [("Sweden", "Stockholm")], [("Norway", "Oslo")]]
# Output:
# [{'country': 'FINLAND', 'city': 'HELSINKI'},
# {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
# {'country': 'NORWAY', 'city': 'OSLO'}]

list = [
    [{"country": country.upper(), "city": capital.upper()}]
    # #  Above line `country` and `capital` is from the last line
    for list in countries
    for (country, capital) in list  # Here `list` is from above line
    # In above line we are destructuring tuple values
]
print(list)
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_13/ex6.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_13/ex6.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_13/ex6.py -->
```py
# Ex6: Change the following list of lists to a list of concatenated strings:
names = [
    [("Asabeneh", "Yetayeh")],
    [("David", "Smith")],
    [("Donald", "Trump")],
    [("Bill", "Gates")],
]
# Output:
# ["Asabeneh Yetaeyeh", "David Smith", "Donald Trump", "Bill Gates"]

list = [
    firstname + " " + lastname
    # Above line `firstname` and `lastname` is from the last line
    for list in names
    for (firstname, lastname) in list  # Here `list` is from above line
]
print(list)
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_13/ex7.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_13/ex7.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_13/ex7.py -->
```py
# Ex7: Write a lambda function which can solve a slope or y-intercept of linear functions.
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
y_intercept = lambda x, y, m: y - (m * x)  # `y=mx+c`

# Example usage
x1, y1 = 0, 1  # First point
x2, y2 = 2, 5  # Second point

m = slope(x1, y1, x2, y2)
b = y_intercept(x1, y1, m)  # when x=0

print(f"Slope (m): {m}")
print(f"Y-intercept (b): {b}")
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_14/1.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_14/1.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_14/1.py -->
```py
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
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_14/2.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_14/2.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_14/2.py -->
```py
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


# * Learn: The reason is that the decorator syntax @decorator can only be used
# * with function definitions (using `def`), not with lambda expressions.


# & Learn: Notice the pattern that `greeting` function is passed as arugment to
# & `uppercase_decorator` function.
@uppercase_decorator
def greeting():
    return "Welcome to Python"


print(greeting())  # WELCOME TO PYTHON
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_14/3.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_14/3.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_14/3.py -->
```py
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
    return resultFn  # This function is always executed in the end.


# & Learn: Notice the pattern that `greeting` function is passed as arugment to
# &     `uppercase_decorator` function. Then `uppercase_decorator` function is passed
# &     as an argument to `split_string_decorator` function.
@split_string_decorator  # * 2nd
@uppercase_decorator  # * 1st
def greeting():  # * 3rd
    print("3 - greetingFunction body")
    return "Welcome to Python"


print(greeting())  # WELCOME TO PYTHON
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_14/4.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_14/4.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_14/4.py -->
```py
# & Accepting Parameters in Decorator Functions
# * Most of the time we need our functions to take parameters, so we might need to
# * define a decorator that accepts parameters.


def logLocationDecorator(logNameFn):
    def resultFn(para1, para2, para3):
        logNameFn(para1, para2, para3)  # `function` here is `printName` function
        print("I live in {}".format(para3))  # Log location

    return resultFn  # This function is always executed in the end.


# & Learn: Notice the pattern that `logName` function is passed as arugment to
# &     `logLocationDecorator` function.
@logLocationDecorator
def logName(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(first_name, last_name, country))


logName("Asabeneh", "Yetayeh", "Finland")
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_14/5.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_14/5.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_14/5.py -->
```py
# * The map() function is a built-in higher order function that takes a function
# *     (i.e., first arugment) and iterates over items over the data (i.e, the
# *     second argument)

# & map() It iterates over a list. For instance, it changes the names to upper
# &         case and returns a new list.
# &         SYNTAX:
# map(function, iterable)

numberList = [1, 2, 3, 4, 5]  # iterable


def square(x):
    return x**2


squaredNumberListSquared = map(square, numberList)  # immutable function
# print(numbers_squared) # Prints address of the map object: <map object at 0x10ed60d30>
print(list(squaredNumberListSquared))  # [1, 4, 9, 16, 25]

# Passing lambda funtion as argument:
squaredNumberListSquared = map(lambda x: x**2, numberList)
# print(numbers_squared) # Prints address of the map object: <map object at 0x10ed60d30>
print(list(squaredNumberListSquared))  # [1, 4, 9, 16, 25]
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_14/6.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_14/6.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_14/6.py -->
```py
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
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_14/7.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_14/7.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_14/7.py -->
```py
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
```
<!-- MARKDOWN-AUTO-DOCS:END -->


## File - `30-days-python-asabeneh/day_14/8.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_14/8.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_14/8.py -->
```py
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
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_14/ex1.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_14/ex1.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_14/ex1.py -->
```py
from functools import reduce

countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland"]
names = ["Asabeneh", "Lidiya", "Ermias", "Abraham"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Ex. Use map to create a new list by changing each country to uppercase in the
#    countries list

uppercase_countries = map(lambda v: v.upper(), countries)
# print(uppercase_countries) # Prints address of the map object: <map object at 0x10ed60d30>
print(list(uppercase_countries))


# Ex. Use filter to filter out countries containing 'land'.
print(list(filter(lambda text: text.find("land") != -1, countries)))

# Ex. Use filter to filter out countries having exactly six characters.
print(list(filter(lambda country: len(country) == 6, countries)))

# Ex. Use filter to filter out countries containing six letters and more in the country list.
print(list(filter(lambda country: len(country) > 6, countries)))

# Ex. Use filter to filter out countries starting with an 'E'
print(list(filter(lambda country: country.startswith("E"), countries)))


# Ex. Declare a function called get_string_lists which takes a list as a
# parameter and then returns a list containing only string items.
def get_string_lists(list1):
    return list(filter(lambda x: type(x) == str, list1))


list1 = ["1", 2, 3, "4", 5, "6"]
print(get_string_lists(list1))  # Output: ["1", "4", "6"]


# Ex. Use reduce to concatenate all the countries and to produce this sentence:
#       Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European
#       countries


def joinCountriesProperly(accumulator, current):
    isLastElement = current == countries[-1]
    if isLastElement:
        return accumulator + ", and " + current
    return accumulator + ", " + current


print(reduce(joinCountriesProperly, countries) + " are north European countries")
```
<!-- MARKDOWN-AUTO-DOCS:END -->


## File - `30-days-python-asabeneh/day_14/utils.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_14/utils.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_14/utils.py -->
```py
import json
import os


# * Prompt to Copilot for reading json file:
#       Read file `countries_data.json` from `data` folder which is present in
#               parent folder of current script.
def readCountriesFromJsonFile():
    dirname = os.path.dirname(os.path.dirname(__file__))
    data_file = os.path.join(dirname, "data", "countries_data.json")

    with open(data_file, "r") as f:
        countries_data = json.load(f)
    return countries_data
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_14/ex2.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_14/ex2.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_14/ex2.py -->
```py
from utils import readCountriesFromJsonFile

# * Ex. 13: Create a function returning a dictionary, where keys stand for starting
#   letters of countries and values are the number of country names starting
#   with that letter.

countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland"]


# & Learn: we get `KeyError: 'bad_key'` when we try to access key which is not defined in dictionary.
a = {"a": 20}
# print(a["badkey"])  # we get exception ---  `KeyError: 'bad_key'`


def get_first_letter_count(country_list):
    dictionary = {}
    for country in country_list:
        firstLetterOfCountry = country[0]
        # & Learn: We use `dictionary.get()` method because if we use dictionary["someBadKey"] then we get exception ---  `KeyError: 'bad_key'`
        dictionary[firstLetterOfCountry] = dictionary.get(firstLetterOfCountry, 0) + 1
    return dictionary


print(get_first_letter_count(countries))


countries = readCountriesFromJsonFile()

# Ex.14: Declare a get_first_ten_countries function - it returns a list of first
#       ten countries from the countries.js list in the data folder.
print(countries[:10])  # get_first_ten_countries

# Ex.15: Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
print(countries[-10:])  # get_last_ten_countries
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_14/ex3.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_14/ex3.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_14/ex3.py -->
```py
from utils import readCountriesFromJsonFile

# Level 3: Sort countries by name, by capital, by population
countries = readCountriesFromJsonFile()
sorted_by_name = sorted(countries, key=lambda x: x["name"])
sorted_by_capital = sorted(countries, key=lambda x: x.get("capital", ""))
sorted_by_population = sorted(countries, key=lambda x: x.get("population", 0))

print("Countries sorted by name:")
print([country["name"] for country in sorted_by_name[:5]])

print("\nCountries sorted by capital:")
print([country["name"] for country in sorted_by_capital[:5]])

print("\nCountries sorted by population:")
print([country["name"] for country in sorted_by_population[:10]])
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_14/ex4.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_14/ex4.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_14/ex4.py -->
```py
from utils import readCountriesFromJsonFile

# Level 3: Sort out the ten most populated countries
countries = readCountriesFromJsonFile()
sorted_countries = sorted(countries, key=lambda x: x["population"], reverse=True)

top_ten = sorted_countries[:10]
print("Ten most populated countries:")

for country in top_ten:
    print(f"{country['name']}: {country['population']:,} people")
```
<!-- MARKDOWN-AUTO-DOCS:END -->


## File - `30-days-python-asabeneh/day_15/1.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_15/1.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_15/1.py -->
```py
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
```
<!-- MARKDOWN-AUTO-DOCS:END -->