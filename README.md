_See older readme: [Click here](./README.old.md) (README.old.md)_

**Quick Links:**
- ❤️ 30 days of pythong: [Click here](https://github.com/Asabeneh/30-Days-Of-Python)
- ❤️ trekhleb/learn-python: [Click here](https://github.com/trekhleb/learn-python)

## Create http server (to show directory listings)

[Source](https://cloudinit.readthedocs.io/en/latest/tutorial/qemu.html)

```bash
# Start the built-in Python webserver:
python3 -m http.server --directory .
```

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

## Learn conda from Corey Schafer

src: [Corey Schafer - Python Tutorial: How I Manage Multiple Projects, Virtual Environments, and Environment Variables](https://youtu.be/cY2NXB_Tqq0?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU)

```bash
# Creating a conda environment
mkdir my_project && cd my_project
# 1. creating a virtual environment along with installing dependencies
conda create --name my_project_env flask [more dependencies]
# 2. activate environment
source activate my_project_env
# 3. create environment.yaml file
conda env export > environment.yaml
# 4. deactivate environment
source deactivate
# (info) show packages installed
pip list
# (info) show all conda environments on current machine
conda env list


# replicating environment on a new machine
conda env create -f environment.yaml

# OTHER: conda auto_env script for .bashrc
# (timestamped) check here (description of video) - https://youtu.be/cY2NXB_Tqq0?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&t=1016

# OTHER: activating env scripts so your env variables automatically changes as you activate the environment
# (timestamped) https://youtu.be/cY2NXB_Tqq0?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&t=501
```

# 30 Days of Python

Code generate via autodocs

## 😇😇😇 Todos:

- Continue exercise of day 5
    - [Content](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/05_Day_Lists/05_lists.md)
    - [Code](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/05_Day_Lists/day_5.py)
- Continue doing exercise of day 19
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
#                   "banana"   "orange"   "mango"   "lemon"
#  Index                0          1          2         3
#  Index from END      -4         -3         -2        -1

# Get first 3 fruits
print(fruits[:3])
# Get last 4 fruits (start from -4 to the end)
print(fruits[-4:])  # ["banana", "orange", "mango", "lemon"]
# Get items starting from -3 to -1(non-inclusive)
print(fruits[-3:-1])  # ['orange', 'mango']         # does not include the end index
# Get last 3 fruits (start from -3 to end)
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

## File - `30-days-python-asabeneh/day_16/1.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_16/1.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_16/1.py -->
```py
import datetime  # `datetime` module to handle date and time

# Using `dir` or `help` built-in commands it is possible to know the available
#       functions in a certain module
print(dir(datetime))
[
    "MAXYEAR",
    "MINYEAR",
    "__builtins__",
    "__cached__",
    "__doc__",
    "__file__",
    "__loader__",
    "__name__",
    "__package__",
    "__spec__",
    "date",
    "datetime",
    "datetime_CAPI",
    "sys",
    "time",
    "timedelta",
    "timezone",
    "tzinfo",
]

print("")

from datetime import datetime

# We will learn about --- date, datetime, time and timedelta function from above:
datetimeNow = datetime.now()  # <class 'datetime.datetime'>
print(type(datetimeNow))
print(datetimeNow)  # 2025-03-25 20:26:48.087765
print(datetimeNow.day)  # 25
print(datetimeNow.month)  # 3
print(datetimeNow.year)  # 2025
print(datetimeNow.hour)  # 20
print(datetimeNow.minute)  # 27
print(datetimeNow.second)  # 10
# Timestamp or Unix timestamp is the number of seconds elapsed from 1st of January 1970 UTC
print(datetimeNow.timestamp())  # 1742914630.235397

print("\n\nPassing argument to datetime(..)")
newYear = datetime(2020, 1, 1)
print(newYear)
# Output: 2020-01-01 00:00:00

print(
    newYear.day,
    newYear.month,
    newYear.year,
    newYear.hour,
    newYear.minute,
    newYear.second,
)
# Output: 1 1 2020 0 0 0

print(
    f"{newYear.day}/{newYear.month}/{newYear.year}, {newYear.hour}:{newYear.minute}:{newYear.second}"
)
# Output: 1/1/2020, 0:0:0
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_16/2.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_16/2.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_16/2.py -->
```py
from datetime import datetime, date, time

# * 🚀 Learn strftime - To parse datetime from string
# Docs: https://strftime.org/
#       The full set of format codes supported varies across
#       platforms, because Python calls the platform C
#       library's strftime() function, and platform
#       variations are common.
# * Linux C Library Docs of strftime (from above docs page):
#       https://man7.org/linux/man-pages/man3/strftime.3.html

datetimeNow = datetime.now()  # current date and time

print(type(datetimeNow.strftime("%H:%M:%S")))  # <class 'str'>

print("H:M:S:", datetimeNow.strftime("%H:%M:%S"))
# Output: H:M:S: 20:39:24

print("mm/dd/YY H:M:S", datetimeNow.strftime("%m/%d/%Y, %H:%M:%S"))
# Output: mm/dd/YY H:M:S 03/25/2025, 20:39:24

print("dd/mm/YY H:M:S", datetimeNow.strftime("%d/%m/%Y, %H:%M:%S"))
# Output: dd/mm/YY H:M:S 25/03/2025, 20:39:24

print("\n\n--------------------------------")

# * 🚀 Learn `strptime` function - To parse datetime from string
datetimeString = "5 December, 2019"
datetime1 = datetime.strptime(datetimeString, "%d %B, %Y")
print(type(datetime1))  # <class 'datetime.datetime'>
print(datetime1)  # 2019-12-05 00:00:00


print("----------------- ")

# * Learn date function

date1 = date(2020, 1, 1)
print(date1)  # 2020-01-01
print("Current date:", date1.today())  # 2025-03-25
print(type(date1.today()))  # <class 'datetime.date'>

# date object of today's date #
dateToday = date.today()
print(type(dateToday.today()))  # <class 'datetime.date'>
print("\nCurrent year:", dateToday.year)  # 2025
print("Current month:", dateToday.month)  # 3
print("Current day:", dateToday.day)  # 25


# * 🚀 Learn `time` function
# Default time: 00:00:00:00 (hour:minute:second:microsecond)
time1 = time()
print("a =", time1)  # 00:00:00
print(type(time1))  # <class 'datetime.time'>

time1 = time(10, 30, 50)
print("b =", time1)  # 10:30:50

time1 = time(hour=10, minute=30, second=50)
print("c =", time1)  # 10:30:50

# Passsing Arguments: time(hour, minute, second, microsecond)
time1 = time(10, 30, 50, 200555)
print("d =", time1)  # 10:30:50.200555
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_16/3.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_16/3.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_16/3.py -->
```py
from datetime import date, datetime

####### * Difference Between Two Points in Time ########
today = date(year=2019, month=12, day=5)
new_year = date(year=2020, month=1, day=1)

time_left_for_newyear = new_year - today

# print(type(time_left_for_newyear))  # <class 'datetime.timedelta'>
print("Time left for new year: ", time_left_for_newyear)  # 27 days, 0:00:00

t1 = datetime(year=2019, month=12, day=5, hour=0, minute=59, second=0)
t2 = datetime(year=2020, month=1, day=1, hour=0, minute=0, second=0)
diff = t2 - t1

print("Time left for new year:", diff)  # 26 days, 23:01:00


####### * Difference Between Two Points in Time via timedelta function
from datetime import timedelta

t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3 =", t3)  #  86 days, 22:56:50
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_16/ex1.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_16/ex1.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_16/ex1.py -->
```py
from datetime import date, datetime, timedelta

# ex.1: Format the current date using this format:
format = "%m/%d/%Y, %H:%M:%S"
currentDatetime = datetime.now()  # current date and time
print(currentDatetime.strftime(format))

# ex.3: Today is 5 December, 2019. Change this time string to time
datetimeString = "5 December, 2019"
datetimeNow = datetime.strptime(datetimeString, "%d %B, %Y")
print(datetimeNow)  # 2019-12-05 00:00:00
print(type(datetimeNow))  # <class 'datetime.datetime'>

# ex.4 Calculate the time difference between now and new year.
datetimeNow = datetime.now()
# (arguments order: year, month, day, hour, minute, second, microsecond)
datetimeNewYear1 = datetime(2026, 1, 1)
datetimeNewYear2 = datetime(year=2026, month=1, day=1, hour=0, minute=0, second=0)

print(datetimeNewYear1 - datetimeNow)  # way1
print(datetimeNewYear2 - datetimeNow)  # way2


# ex.5 Calculate the time difference between 1 January 1970 and now
datetimeNow = datetime.now()
datetime1970 = datetime(1970, 1, 1)
print(datetimeNow - datetime1970)
```
<!-- MARKDOWN-AUTO-DOCS:END -->


## File - `30-days-python-asabeneh/day_17/1.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_17/1.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_17/1.py -->
```py
# try:
#       code in this block if things go well
# except: # (May or may not have a condition)
#       code in this block run if things go wrong

try:
    name = input("Enter your name:")
    year_born = input("Year you born:")
    age = 2019 - int(year_born)
    print(f"You are {name}. And your age is {age}.")
except TypeError:
    print("Type error occur")
except ValueError:
    print("Value error occur")
except ZeroDivisionError:
    print("zero division error occur")
else:  # This runs without when there is no exception:
    print("I usually run with the try block")
finally:
    print("I alway run.")
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_17/2.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_17/2.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_17/2.py -->
```py
# Shorter version of above code:
try:
    name = input("Enter your name:")
    year_born = input("Year you born:")  # * Try inputing string here to trigger error.
    age = 2025 - int(year_born)
    print(f"You are {name}. And your age is {age}.")
except Exception as e:  # * Catching all exceptions in a single instruction.
    print("Sorry we got exception:", e)
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_17/3.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_17/3.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_17/3.py -->
```py
# & Packing and Unpacking Arguments in Python
# & We use two operators:
# &     1. Python uses * for tuples
# &     2. Python uses ** for dictionaries


def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e


lst = [1, 2, 3, 4, 5]

# Below instruction throws: TypeError: sum_of_five_nums() missing 4 required positional arguments: 'b', 'c', 'd', and 'e'
# print(sum_of_five_nums(lst))

# unpack/destructure the list
print(sum_of_five_nums(*lst))

# Destructuting/Unpacking `range(..)`
numbers = range(2, 7)  # normal call with separate arguments
print(numbers)  # range(2, 7)
print(list(numbers))  # [2, 3, 4, 5, 6]

# Passing list (array) of values as `args` to function via destructuting/unpacking
args = [2, 7]
numbers = range(*args)  # call with arguments unpacked from a list
print(numbers)  # [2, 3, 4, 5,6]


# * list destructuring/unpacking
countries = ["Finland", "Sweden", "Norway", "Denmark", "Iceland"]
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest)  # Finland Sweden Norway ['Denmark', 'Iceland']

# * tuple destructuring/unpacking
numbers = (1, 2, 3, 4, 5, 6, 7)
one, *middle, last = numbers
print(one, middle, last)  #  1 [2, 3, 4, 5, 6] 7


# * Unpacking Dictionaries
def unpacking_person_info(name, country, city, age):
    return f"{name} lives in {country}, {city}. He is {age} year old."


dct = {"name": "Sahil", "country": "India", "city": "Chandigarh", "age": 250}
print(unpacking_person_info(**dct))
# Output Sahil lives in India, Chandigarh. He is 1750 years old.


# * Packing Dictionaries
def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s


print(sum_all(1, 2, 3))  # 6
print(sum_all(1, 2, 3, 4, 5, 6, 7))  # 28


# & Packing Dictionaries
# `kwargs` stands for "keyword arguments"
# * Learn: Appening ** before an argument allows a function to accept any number of keyword arguments
def packing_person_info(**kwargs):
    print(type(kwargs))  # <class 'dict'>
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    return kwargs


# Passing keyword arguments to function call:
print(packing_person_info(name="Asabeneh", country="Finland", city="Helsinki", age=250))

# * List Spreading (like spreading in javascript)
lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *lst_one, *lst_two]
print(lst)  # [0, 1, 2, 3, 4, 5, 6, 7]

country_lst1 = ["Finland", "Sweden", "Norway"]
country_lst2 = ["Denmark", "Iceland"]
nordic_countries = [*country_lst1, *country_lst2]
print(nordic_countries)  # ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']


# * Enumerate
# If we are interested in an index of a list, we use `enumerate ()` built-in function to get the index of each item in the list.

for index, item in enumerate([20, 30, 40]):
    print(index, item)
    # Output:
    # 0 20
    # 1 30
    # 2 40

countries = ["Finland", "Sweden", "Norway", "Denmark", "Iceland"]
for index, country in enumerate(countries):
    print("hi", index)
    if country == "Finland":
        print(f"The country {country} has been found at index {index}")
        # Output:
        # hi 0
        # The country Finland has been found at index 0
        # hi 1
        # hi 2
        # hi 3
        # hi 4


# * Zip - To loop over two lists using a single for loop instead of two nested for loops
fruits = ["banana", "orange"]
veges = ["Tomato", "Potato"]  # (vegetables)
fruits_and_veges = []
for fruit, veg in zip(fruits, veges):
    fruits_and_veges.append({"fruit": fruit, "veg": veg})
print(fruits_and_veges)
# [{'fruit': 'banana', 'veg': 'Tomato'}, {'fruit': 'orange', 'veg': 'Potato'}]

# Doing above functioning without using `zip`
fruits_and_veges = []
for i in range(len(fruits)):
    fruits_and_veges.append({"fruit": fruits[i], "veg": veges[i]})
print(fruits_and_veges)
# [{'fruit': 'banana', 'veg': 'Tomato'}, {'fruit': 'orange', 'veg': 'Potato'}]
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_17/ex1.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_17/ex1.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_17/ex1.py -->
```py
# Unpack the first five countries and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively.
names = ["Finland", "Sweden", "Norway", "Denmark", "Iceland", "Estonia", "Russia"]
*firstFiveCountries, es, ru = names
print(firstFiveCountries)
print(es)
print(ru)
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_18/1.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_18/1.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_18/1.py -->
```py
import re

# * A regular expression or RegEx is a special text string
#       that helps to find patterns in data. A RegEx can be used
#       to check if some pattern exists in a different data type.
#       To use RegEx in python first we should import the RegEx
#       module which is called re.

# * Methods in re Module
#   To find a pattern we use different set of re character sets that allows to search for a match in a string.
#       - re.match(): searches only in the beginning of the first line
#       of the string and returns matched objects if found, else
#       returns None.
#        - re.search: Returns a match object if there is
#           one anywhere in the string, including multiline strings.
#       - re.findall: Returns a list containing all matches
#       - re.split: Takes a string, splits it at the match points,
#           returns a list
#       - re.sub: Replaces one or many matches within a string

# & SYNTAX (re.I to ignore case)
# re.match(STRING_OR_PATTERN, INPUT_TEXT, re.I)

inputText = "I love to teach python and javaScript"
# It returns an object with span, and match
searchText = "I love to teach"
# print(len(searchText))  # 15

#  The match function returns an object only if the `txt` starts with the pattern
match = re.match(searchText, inputText, re.I)
print(match)  # <re.Match object; span=(0, 15), match='I love to teach'>

# * Using span() we get starting and ending position of the match as tuple
print(match.span())  # (0, 15)

# Destructure start and end from `span`
start, end = match.span()
print(start, end)  # 0, 15

# * awesome
substring = inputText[start:end]
print(substring)  # I love to teach

# inline way (looks a little dirty though)
print(inputText[match.span()[0] : match.span()[1]])  # I love to teach


# when searchText is not found in inputText
inputText = "I love to teach python and javaScript"
match = re.match("Baburaav ghr pe hai?", inputText, re.I)
print(match)  # None


print(" ---------------------------------")


# & re.search
# SYNTAX: re.search(STRING_OR_PATTERN, INPUT_TEXT, re.I)

# re.search is much better than re.match because it can look for the pattern
#       throughout the text. re.search returns a match object with a first
#       match that was found, otherwise it returns None.

inputText = """Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language"""

# It returns an object with span and match
match = re.search("first", inputText, re.I)
print(match)  # <re.Match object; span=(100, 105), match='first'>

# * Using span() we get starting and ending position of the match as tuple
span = match.span()
print(span)  # (100, 105)

# Lets find the start and stop position from the span
start, end = span
print(start, end)  # 100 105

substring = inputText[start:end]
print(substring)  # first


# & re.findall - Searching for *all* matches
matches = re.findall("language", inputText, re.I)
print(matches)  # ['language', 'language']

matches = re.findall("python", inputText, re.I)
print(matches)  # ['Python', 'python']

# Way 1 to search for python or Python without using re.I
matches = re.findall("Python|python", inputText)
print(matches)  # ['Python', 'python']

# Way 2 to search for python or Python without using re.I
matches = re.findall("[Pp]ython", inputText)
print(matches)  # ['Python', 'python']
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_18/2.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_18/2.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_18/2.py -->
```py
import re

# & Replacing a Substring
# & =====================
inputText = """Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language"""

match_replaced = re.sub("Python|python", "JavaScript", inputText, re.I)
print(match_replaced)
# Output: JavaScript is the most beautiful language that a human being has ever created. I recommend JavaScript for a first programming language

# OR

match_replaced = re.sub("[Pp]ython", "JavaScript", inputText, re.I)
print(match_replaced)
# Output: JavaScript is the most beautiful language that a human being has ever created. I recommend JavaScript for a first programming language


print("-----------------------")

inputText = """%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?"""

matches = re.sub("%", "", inputText)
print(matches)
# Output:
# I am teacher and  I love teaching.
# There is nothing as rewarding as educating and empowering people.
# I found teaching more interesting than any other jobs.
# Does this motivate you to be a teacher?


print("-----------------------")

inputText = """I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?"""

print(re.split("\n", inputText))  # splitting using \n - end of line symbol
# Output:
# [
#     "I am teacher and  I love teaching.",
#     "There is nothing as rewarding as educating and empowering people.",
#     "I found teaching more interesting than any other jobs.",
#     "Does this motivate you to be a teacher?",
# ]

# & Writing RegEx Patterns
regexPattern = r"apple"
inputText = "Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. "

matches = re.findall(regexPattern, inputText)
print(matches)  # ['apple']

# case insensitive search
matches = re.findall(regexPattern, inputText, re.I)
print(matches)  # ['Apple', 'apple']

# Or we can use a set of characters method i.e, [Aa]  --- this mean the first letter could be A or a
regexPattern = r"[Aa]pple"
matches = re.findall(regexPattern, inputText)
print(matches)  # ['Apple', 'apple']

# & Writing RegEx Patterns
# & ======================

# []: A set of characters
#   [a-c] means, a or b or c
#   [a-z] means, any letter from a to z
#   [A-Z] means, any character from A to Z
#   [0-3] means, 0 or 1 or 2 or 3
#   [0-9] means any number from 0 to 9
#   [A-Za-z0-9] any single character, that is a to z, A to Z or 0 to 9
# \: uses to escape special characters
#   \d means: match where the string contains digits (numbers from 0-9)
#   \D means: match where the string does not contain digits
# . : any character except new line character(\n)
# ^: starts with
#   r"^substring" eg r"^love", a sentence that starts with a word love
#   r"[^abc]" means not a, not b, not c.
# $: ends with
#   r"substring$" eg r"love$", sentence that ends with a word love
# *: zero or more times
#   r"[a]*" means a optional or it can occur many times.
# +: one or more times
#   r"[a]+" means at least once (or more)
# ?: zero or one time
#   r"[a]?" means zero times or once
# {3}: Exactly 3 characters
# {3,}: At least 3 characters
# {3,8}: 3 to 8 characters
# |: Either or
#   r"apple|banana" means either apple or a banana
# (): Capture and group

# & Square Bracket
regexPattern = r"[Aa]pple"  # this square bracket mean either A or a
matches = re.findall(regexPattern, inputText)
print(matches)  # ['Apple', 'apple']

# Using square brackets and or (|) operator - we extract Apple, apple, Banana, banana
regexPattern = r"[Aa]pple|[Bb]anana"
inputText = "Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away."
matches = re.findall(regexPattern, inputText)
print(matches)  # ['Apple', 'banana', 'apple', 'banana']


# & Escape character(\)
regexPattern = r"\d"  # d is a special character which means digits
inputText = "This regular expression example was made on December 6,  2019 and revised on July 8, 2021"
matches = re.findall(regexPattern, inputText)
print(matches)
# ['6', '2', '0', '1', '9', '8', '2', '0', '2', '1']

# & One or more times(+)
# d is a special character which means digits, + mean one or more times
regexPattern = r"\d+"
inputText = "This regular expression example was made on December 6,  2019 and revised on July 8, 2021"
matches = re.findall(regexPattern, inputText)
print(matches)  # ['6', '2019', '8', '2021'] - now, this is better!

print("------------------------------ ")

# & Period(.) - Any character except new line character
inputText = """Apple and banana are fruits"""
# The square bracket means a and . means any character except new line
regexPattern = r"[a]."
matches = re.findall(regexPattern, inputText)
print(matches)  # ['an', 'an', 'an', 'a ', 'ar'] # ✅

# . means any character except new line character, + means any character one or more times
regexPattern = r"[a].+"
matches = re.findall(regexPattern, inputText)
print(matches)  # ['and banana are fruits'] # ✅✅


# & Asterisk(*) - Any character ZERO or MORE TIMES
# . means any character, * any character zero or more times
regexPattern = r"[a].*"
inputText = """Apple and banana are fruits"""
matches = re.findall(regexPattern, inputText)
print(matches)  # ['and banana are fruits'] # ✅

# & (?) - Any character ZERO or ONE TIME
# Zero or one time. The pattern may not occur or it may occur once.

inputText = """I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail."""
regexPattern = r"[Ee]-?mail"  # ? means here that '-' is optional
matches = re.findall(regexPattern, inputText)
print(matches)  # ['e-mail', 'email', 'Email', 'E-mail'] # ✅

# & Quantifier ({})
# We can specify the length of the substring we are looking for in a
#       text, using a curly bracket. Let us imagine, we are interested in a
#       substring with a length of 4 characters:
inputText = "This regular expression example was made on December 6,  2019 and revised on July 8, 2021"
regexPattern = r"\d{4}"  # exactly four times
matches = re.findall(regexPattern, inputText)
print(matches)  # ['2019', '2021']

inputText = "This regular expression example was made on December 6,  2019 and revised on July 8, 2021"
regexPattern = r"\d{1, 4}"  # 1 to 4
matches = re.findall(regexPattern, inputText)
print(matches)  # ['6', '2019', '8', '2021']


# & Cart ^ (❤️)
#  1. Starts with
inputText = "This regular expression example was made on December 6,  2019 and revised on July 8, 2021"
regexPattern = r"^This"  # ^ means starts with
matches = re.findall(regexPattern, inputText)
print(matches)  # ['This']

# 2. Negation
txt = "This regular expression example was made on December 6,  2019 and revised on July 8, 2021"
regex_pattern = r"[^A-Za-z ]+"  # ^ in set character means negation, not A to Z, not a to z, no space
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6,', '2019', '8', '2021']
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## Regex Pattern Chart from course

![](./30-days-python-asabeneh/images/regex-chart.png)

## File - `30-days-python-asabeneh/day_18/ex1.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_18/ex1.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_18/ex1.py -->
```py
import re

# ex1: What is the most frequent word in the following paragraph?

paragraph = "I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love."

# Regex Explanation:
#   \W matches any non-word character (opposite of \w which matches [a-zA-Z0-9_])
#   + means "one or more occurrences"
words = re.split(r"\W+", paragraph.lower())
wordsCount = {}

for word in words:
    if word:  # Skip empty strings
        wordsCount[word] = wordsCount.get(word, 0) + 1

mostFrequentWord = max(wordsCount.items(), key=lambda x: x[1])
print(mostFrequentWord)
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_18/ex2.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_18/ex2.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_18/ex2.py -->
```py
import re

# ex2. The position of some particles on the horizontal x-axis are
#       -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8
#       in the positive direction. Extract these numbers from this whole
#       text and find the distance between the two furthest particles.

# *EXPECTED RESULTS*
# points = ["-12", "-4", "-3", "-1", "0", "4", "8"]
# sorted_points = [-12, -4, -3, -1, -1, 0, 2, 4, 8]
# distance = 8 - (-12)  # 20

# Solution:
inputText = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles."
points = re.findall(r"-?\d+", inputText)
points = [int(p) for p in points]  # converting str to int via list comprehension
print(points)  # [-12, -4, -3, -1, 0, 4, 8]
sorted_points = sorted(points)  # [-12, -4, -3, -1, 0, 4, 8]

# distance b/w most extreme points
distance = sorted_points[-1] - sorted_points[0]
print(f"\nDistance between furthest points: {distance}")
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_18/ex3.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_18/ex3.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_18/ex3.py -->
```py
import re

# ex3. Write a pattern which identifies if a string is a valid python variable


# Using regex (solution for exercise purpose)
def is_valid_variable(name):
    pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
    return print(bool(re.match(pattern, name)))


# * Solution with idiomatic Code (without using regex)
# def is_valid_variable(name):
#     if not name.isidentifier():
#         return print(False)
#     return print(True)


# Test cases from exercise
is_valid_variable("first_name")  # True
is_valid_variable("first-name")  # False
is_valid_variable("1first_name")  # False
is_valid_variable("firstname")  # True
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_18/ex4.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_18/ex4.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_18/ex4.py -->
```py
import re

# Clean the following text. After cleaning, count three most frequent
#       words in the string.
sentence = """%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?"""
# Clean the text using regex to remove special characters
clean_sentence = re.sub(r"[%$@#&;!?,.]", "", sentence)

# From exercise
expectedSentence = "I am a teacher and I love teaching There is nothing as more rewarding as educating and empowering people I found teaching more interesting than any other jobs Does this motivate you to be a teacher"
if clean_sentence == expectedSentence:
    print("Sentence cleaning successful ✅")
else:
    print("Sentence cleaning FAILED 🛑")

# Split into words and count frequencies
words = clean_sentence.split()
wordsCount = {}
for word in words:
    wordsCount[word] = wordsCount.get(word, 0) + 1

# Get 3 most frequent words
mostCountWord = sorted(wordsCount.items(), key=lambda x: x[1], reverse=True)[:3]
print("Most frequent words:", mostCountWord)
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_19/1.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_19/1.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_19/1.py -->
```py
# & File Handling
# * Syntax:
# open("filename", mode)
# where `mode` can be r, a, w, x, t, b  could be to read, write, update.
# * "r" - Read - Default value. Opens a file for reading, it returns an error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# * "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

import os

dirname = os.path.dirname(__file__)
filePath = os.path.join(dirname, "reading_file_example.txt")

f = open(filePath)
# print(f) # Output: <_io.TextIOWrapper name='./files/reading_file_example.txt' mode='r' encoding='UTF-8'>
txt = f.read()  # <class 'str'>
f.close()  # An opened file has to be closed with close() method.

print(type(txt))
print(txt)
# Output:
"""
This is an example to show how to open a file and read.
This is the second line of the text.
"""

# * Instead of printing all the text, let us print the first 10 characters of the text file.
f = open(filePath)
txt = f.read(10)
print(txt)  # Output: This is an
f.close()


# * readline(): read only the first line
f = open(filePath)
line = f.readline()
print(line)  # This is an example to show how to open a file and read.
f.close()

# * readlines(): read all the text line by line and returns a list of lines
f = open(filePath)
lines = f.readlines()
f.close()
print(type(lines))  # # <class 'list'>
print(lines)  #
[
    "This is an example to show how to open a file and read.\n",
    "This is the second line of the text.",
]

# * splitlines(): To get all the lines as a list
f = open(filePath)
lines = f.read().splitlines()
f.close()
print(type(lines))  # <class 'list'>
print(lines)
# ['This is an example to show how to open a file and read.', 'This is the second line of the text.']

print("------------------------------")

# & After we open a file, we should close it. There is a high tendency of forgetting to close them. There is a new way of opening files using with - closes the files by itself. Let us rewrite the the previous example with the with method:
with open(filePath) as f:
    lines = f.read().splitlines()
    print(type(lines))  # <class 'list'>
    print(lines)
    # ['This is an example to show how to open a file and read.', 'This is the second line of the text.']


# & Opening Files for Writing and Updating
# To write to an existing file, we must add a mode as parameter to the open() function:

# "a" - append - will append to the end of the file, if the file does not it creates a new file.
# "w" - write - will overwrite any existing content, if the file does not exist it creates.

# * Let us append some text to the file we have been reading:
filePath = os.path.join(dirname, "file2.txt")  # & Using `file2.txt` now
with open(filePath, "a") as f:
    f.write("This text has to be appended at the end. ")

# * The method below creates a new file, if the file does not exist:
filePath = os.path.join(dirname, "file3.txt")  # & Using `file2.txt` now
with open(filePath, "w") as f:
    f.write("This text will be written in a newly created file")


# * Deleting Files
filePath = os.path.join(dirname, "NON_EXISTING_FILE.txt")  # & Using `file2.txt` now
# If the file does not exist, the remove() method will raise an error `FileNotFoundError`,
#       so it is good to use a condition like this:
if os.path.exists(filePath):
    os.remove(filePath)
else:
    print("The file does not exist")

# & File with json Extension
# JSON stands for JavaScript Object Notation. Actually, it is a stringified JavaScript object or Python dictionary.
# dictionary
person1 = {
    "name": "Sahil",
    "country": "India",
    "city": "Chandigarh",
    "skills": ["JavaScrip", "React", "Python"],
}
# JSON: A string form a dictionary
json1 = "{'name': 'Sahil', 'country': 'India', 'city': 'Chandigarh', 'skills': ['JavaScrip', 'React', 'Python']}"

# we use three quotes and make it multiple line to make it more readable
json1 = """{
    "name":"Sahil",
    "country":"India",
    "city":"Chandigarh",
    "skills":["JavaScrip", "React","Python"]
}"""

# & Converting json to dictionary
# To change a JSON to a dictionary, first we import the json module and then we use loads method.
import json

json1 = """{
    "name": "Sahil",
    "country": "India",
    "city": "Chandigarh",
    "skills": ["JavaScrip", "React", "Python"]
}"""

person1 = json.loads(json1)

print(type(person1))  # <class 'dict'>
print(person1)
# Output: {'name': 'Sahil', 'country': 'India', 'city': 'Chandigarh', 'skills': ['JavaScrip', 'React', 'Python']}

print(person1["name"])  # Sahil

# & Saving dictionary as a JSON File
# We can also save our data as a json file. Let us save it as a json
#       file using the following steps. For writing a json file, we use the
#       json.dump() method, it can take dictionary, output file,
#       ensure_ascii and indent.  we use encoding and indentation.
#       Indentation makes the json file easy to read.

person1 = {
    "name": "Sahil",
    "country": "India",
    "city": "Chandigarh",
    "skills": ["JavaScrip", "React", "Python"],
}

filePath = os.path.join(dirname, "json_example.json")  # & Using `json_example.json` now
with open(filePath, "w", encoding="utf-8") as f:
    json.dump(person1, f, ensure_ascii=False, indent=4)


# & Reading a csv file
# CSV stands for comma separated values. CSV is a simple file format
#       used to store tabular data, such as a spreadsheet or database. CSV
#       is a very common data format in data science.
# Example:
""""
"name","country","city","skills"
"Asabeneh","Finland","Helsinki","JavaScript"
"""

import csv

filePath = os.path.join(dirname, "myCSVfile.csv")  # & Using `myCSVfile.csv` now
with open(filePath) as f:
    csv_reader = csv.reader(f, delimiter=",")  # we use, reader() method to read csv
    line_count = 0
    for entry in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(entry)}')
            # Output: Column names are name, country, city, skills
        else:
            print(f"\t{entry[0]} is a teachers. He lives in {entry[1]}, {entry[2]}.")
            # Output: Sahil is a teachers. He lives in India, Chandigarh.
        line_count += 1
    print(f"Number of lines:  {line_count}")  # 2

# & File with xlsx Extension
# To read excel files we need to install xlrd package. We will cover this after we cover package installing using pip.
# import xlrd
# excel_book = xlrd.open_workbook('sample.xls)
# print(excel_book.nsheets)
# print(excel_book.sheet_names)


print("-----------------------------------")

# & File with xml Extension
# XML is another structured data format which looks like HTML. In XML
#       the tags are not predefined. The first line is an XML declaration.
#       The person tag is the root of the XML. The person has a gender
#       attribute. Example:XML

"""
<?xml version="1.0"?>
<person gender="female">
  <name>Asabeneh</name>
  <country>Finland</country>
  <city>Helsinki</city>
  <skills>
    <skill>JavaScrip</skill>
    <skill>React</skill>
    <skill>Python</skill>
  </skills>
</person>
"""

# For more information on how to read an XML file check the documentation at https://docs.python.org/2/library/xml.etree.elementtree.html

import xml.etree.ElementTree as ET

filePath = os.path.join(dirname, "myXMLfile.xml")  # & Using `myXMLfile.xml` now
tree = ET.parse(filePath)
root = tree.getroot()
print("Root tag:", root.tag)  # person
print("Attribute:", root.attrib)  # {'gender': 'female'}
for child in root:
    print("field: ", child.tag)
    # Output:
    # field:  name
    # field:  country
    # field:  city
    # field:  skills
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_19/ex1.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_19/ex1.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_19/ex1.py -->
```py
# ex1: Write a function which count number of lines and number of words in a text. All the files are in the data the folder: a) Read obama_speech.txt file and count number of lines and words.

import os
import re

dirname = os.path.dirname(__file__)
filePath = os.path.join(dirname, "..", "data", "obama_speech.txt")

with open(filePath) as f:
    lines = f.readlines()
    print(len(lines))  # 66


with open(filePath) as f:
    txt = f.read()
    # Regex Explanation:
    #   \W matches any non-word character (opposite of \w which matches [a-zA-Z0-9_])
    #   + means "one or more occurrences"
    words = re.split(r"\W+", txt.lower())
    print(len(words))  # 2402
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_19/ex2.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_19/ex2.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_19/ex2.py -->
```py
from utils import readCountriesFromJsonFile

# ex2: Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages

countries = readCountriesFromJsonFile()
# print(countries)
# Output:
#  [{
#     "name": "Norway",
#     "capital": "Oslo",
#     "languages": [
#         "Norwegian",
#         "Norwegian Bokmål",
#         "Norwegian Nynorsk"
#     ],
#     "population": 5223256,
#     "flag": "https://restcountries.eu/data/nor.svg",
#     "currency": "Norwegian krone"
# }]
print("")


def most_spoken_languages(countries, n):
    languages = {}
    for country in countries:
        for language in country["languages"]:
            if language in languages:
                languages[language] += 1
            else:
                languages[language] = 1
    # print(languages.items()) # dict_items([('Pashto', 1), ('Uzbek', 2),..])
    # print(type(languages.items())) # <class 'dict_items'>
    sorted_languages = sorted(languages.items(), key=lambda x: x[1], reverse=True)
    return sorted_languages[:n]
    # return sorted_languages[-10:] # (Get least spoken languages)


mostSpokenLanguages = most_spoken_languages(countries, 10)
for mostSpokenLanguage in mostSpokenLanguages:
    print(mostSpokenLanguage)
```
<!-- MARKDOWN-AUTO-DOCS:END -->

# 🛑🛑🛑🛑Todo: continue doing exercise of day 19🛑🛑🛑🛑
