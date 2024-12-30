_See older readme: [Click here](./README.old.md) (README.old.md)_

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

- 😇😇😇 Continue doing day 4's exercise from 11th point
    - [Content](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/04_Day_Strings/04_strings.md)
    - CODE - [day4.py](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/04_Day_Strings/day_4.py
- (future todos to add here))

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
# 1. From Python 3.6 (2016) we use this `f-strings` syntax widely for their readability and efficiency
# when formatting strings.)
# 2. This approach is concise and more efficient compared to older methods like str.format() or string concatenation.


# Using str.format()                        (Way 2)
print(
    "{}, good to meet you!".format(x)
)  # You can use single ('') or double ("") quotes as you wish

# ###
# Note: Both methods (`f-strings` & `str.format`) allow you to include multiple variables in a string, but f-strings are generally preferred for their cleaner syntax.
# ###
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
pto = language[0:6:2]  #
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

# PRINTS ALL THE POINTS IN TWO-DIMENSION SPACE.
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
# We learn in this example that we can pass a condition after the `for-loop` and return values if that condition passes.

points = [
    [xval, yval, zval]
    for xval in X
    for yval in Y
    for zval in Z
    if myLambda(xval, yval, zval, required_sum)
]  # SOLUTION USING LAMBDA FUNCTION.
print(points)  # [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
# We learn in this example that we can pass a lambda function after the `for-loop` and condition returned from
#   lambda function will judge whether to show a variable


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
# Calculate the area of a circle and assign the value to a variable name of area_of_circle
# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
# Take radius as user input and calculate the area.

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
# source of this file -- https://github.com/Asabeneh/30-Days-Of-Python/blob/master/03_Day_Operators/day-3.py
# Note to Sahil: I have kept only non-repetitive code in this file from above reference file.

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
# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
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
# Find the length of the text python and convert the value to float and convert it to string
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


# Check if int('9.8') is equal to 10
c = int("9.8")
# Above statement throws runtime error: `ValueError: invalid literal for int() with base 10: '9.8'``
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_03/ex4.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_03/ex4.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_03/ex4.py -->
```py
# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
# SAMPLE:
# Enter number of years you have lived: 100
# You have lived for 3153600000 seconds.


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
print(multiline_string)
print()
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
In Python and other programming languages \ followed by a character is an escape sequence. Let us see the most common escape characters:

\n: new line
\t: Tab means(8 spaces)
\\: Back slash
\': Single quote (')
\": Double quote (")
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
# isdigit(): Checks if all characters in a string are numbers (0-9 and some other unicode characters for numbers)
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


# isidentifier():Checks for valid identifier means it check if a string is a valid variable name
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
In Python there are many ways of formatting strings. In this section, we will cover some of them. The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list), together with a format string, which contains normal text together with "argument specifiers", special symbols like "%s", "%d", "%f", "%.number of digitsf".

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
print(
    formated_string
)  # "The following are python libraries:['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']"

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
Another new string formatting is string interpolation, f-strings. Strings start with f and we can inject the data in their corresponding positions.
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
# index(): Returns the lowest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1). If the substring is not found it raises a valueError.
challenge = "thirty days of python"
sub_string = "da"
print(challenge.index(sub_string))  # 7

# print(challenge.index(sub_string, 9))  # runtime error
"""
ValueError: substring not found
"""


# rindex(): Returns the highest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1)
challenge = "thirty days of python"
sub_string = "da"
print(challenge.rindex(sub_string))  # 7
print(challenge.rindex("on", 8))  # 19

# print(challenge.rindex(sub_string, 9))  # runtime error
"""
ValueError: substring not found
"""
```
<!-- MARKDOWN-AUTO-DOCS:END -->
