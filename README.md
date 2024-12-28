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

## Todos:

- start day 3
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
print(3 % 2)  #                                 modulus(%)
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

x = input('Please enter your name\n')
# x = 'Alice' # (Testing)

if type(x) == str:
    print("str type")

# f-strings (formatted string literals)     (Way 1)
print(f"{x}, good to meet you!")            # You can use single ('') or double ("") quotes as you wish
# Note:
# 1. From Python 3.6 (2016) we use this `f-strings` syntax widely for their readability and efficiency
# when formatting strings.)
# 2. This approach is concise and more efficient compared to older methods like str.format() or string concatenation.


# Using str.format()                        (Way 2)
print("{}, good to meet you!".format(x))    # You can use single ('') or double ("") quotes as you wish

# ###
# Note: Both methods (`f-strings` & `str.format`) allow you to include multiple variables in a string, but f-strings are generally preferred for their cleaner syntax.
# ###
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_01/2.2.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_01/2.2.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_01/2.2.py -->
```py
s = 'sahil'
print(len(s)) # 5

if len(s) == 5:
    print('Yes it is a 5.')
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_01/2.3.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_01/2.3.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_01/2.3.py -->
```py
a = 4
b = 3
print(f'{a} + {b} = {a +b}')        # 4 + 3 = 7
print(f'{a} - {b} = {a - b}')       # 4 - 3 = 1
print(f'{a} * {b} = {a * b}')       # 4 * 3 = 12
print(f'{a} / {b} = {a / b:.2f}')   # 4 / 3 = 1.33
print(f'{a} % {b} = {a % b}')       # 4 % 3 = 1
print(f'{a} // {b} = {a // b}')     # 4 // 3 = 1
print(f'{a} ** {b} = {a ** b}')     # 4 ** 3 = 64
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_01/2.4.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_01/2.4.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_01/2.4.py -->
```py
simple = 'Python'
a,b,c,d,e,f = simple # unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_01/2.5.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_01/2.5.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_01/2.5.py -->
```py
language = 'Python'
pto = language[0:6:2] #
print(pto)              # "Pto"
print(type(pto) == str) # True
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_01/3.1.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_01/3.1.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_01/3.1.py -->
```py
# Print weight in pounds, kg.
print('This is weight calculate machine...')

def toKg(pounds):
  return pounds/2.2046


def toPounds(kg):
  return kg * 2.2046


def userInput():
  print('Q. Please choose pounds or kgs (p/k)...')
  choice = input('')
  if choice == 'p':
    print('You choose pounds!!')
    pounds = int(input())
    print(toKg(pounds))
    
  elif choice == 'k':
    print('You choose kgs')
    kg = int(input())
    print(toPounds(kg))
  else:
    print('You choose wrong, choose again!')
    userInput()

userInput()
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_01/3.2.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_01/3.2.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_01/3.2.py -->
```py
# Nested list comprehension example.
myLambda = lambda a, b, sum: a + b != sum # Returns True or False

X = range(3) # [0, 1, 2 , ...n-1]
Y = range(2)

# PRINTS ALL THE POINTS IN TWO-DIMENSION SPACE.
points = [[xval, yval] for xval in X for yval in Y] # Prints all the points.
print(points) # [[0, 0], [0, 1], [1, 0], [1, 1], [2, 0], [2, 1]]

# Note to Sahil: This above syntax of nested loop works like
# `for Loop1 for Loop2`
# Loop1 (e.g., X values in this case)
#       Loop2 (e.g, Y values in this case)



# Print values only when sum of values is `required_sum`
required_sum = 3

points = [[xval, yval] for xval in X for yval in Y if xval+yval != required_sum] # SIMPLE SOLUTION.
print(points) # [[0, 0], [0, 1], [1, 0], [1, 1], [2, 0]]
# We learn in this example that we can pass a condition after the `for-loop` and return values if that condition passes.


points = [[xval, yval] for xval in X for yval in Y if myLambda(xval, yval, required_sum)] # SOLUTION USING LAMBDA FUNCTION.
print(points) # [[0, 0], [0, 1], [1, 0], [1, 1], [2, 0]]
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
myLambda = lambda a, b, c, sum: a + b + c != sum # Returns True or False

X = range(2) # [0, 1, 2 , ...n-1]
Y = range(2)
Z = range(2)

# PRINTS ALL THE POINTS IN SPACE.
points = [[xval, yval, zval] for xval in X for yval in Y for zval in Z] # Prints all the points.
print(points) # [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]



# Print values only when sum of values is `required_sum`
required_sum = 2

points = [[xval, yval, zval] for xval in X for yval in Y for zval in Z if xval+yval+zval != required_sum] # SIMPLE SOLUTION.
print(points) # [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
# We learn in this example that we can pass a condition after the `for-loop` and return values if that condition passes.

points = [[xval, yval, zval] for xval in X for yval in Y for zval in Z if myLambda(xval, yval, zval, required_sum)] # SOLUTION USING LAMBDA FUNCTION.
print(points) # [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
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
secret_number = 7 # right number

count = 1

allowed_attempts = 3

def game(count):
  i = int(input(f'You have {allowed_attempts} attempts to guess the number. \nTry your luck, choose a number:\n'))
  count += 1
  if i == secret_number:
    print('Hooray..!')
  else:
    if count > allowed_attempts:
      print('Sorry, You loose!!')
      return # terminate the function execution.
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
  if choice == 'help':
    print(info)
    game(is_started)
  elif choice == 'start':
    if is_started == True:
      print('You car is already started🥶︎!')
      game(is_started)
    print('Your car started..🚀︎🚀︎!!.')
    is_started = True
    game(is_started)
  elif choice == 'stop':
    if is_started == False:
      print('You car is already stopped🥶︎!')
      game(is_started)
    print('You car stopped ..🛑︎🛑︎')
    is_started = False
    game(is_started)
  elif choice == 'quit':
    print('Thanks for playing the game 🧸︎')
    return
  else:
    print("I don't understand that...")
    print('Try again..')
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

# print(text.join(' Sahil')) # bakchodi


person_info = {
    "firstname": "Asabeneh",
    "lastname": "Yetayeh",
    "country": "Finland",
    "city": "Helsinki",
}

print(person_info)
```
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_02/1.py -->
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
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_02/2.py -->
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
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_02/3.py -->
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_02/ex01.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_02/ex01.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_02/ex01.py -->
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
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_02/ex01.py -->
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_02/ex02.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_02/ex02.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_02/ex02.py -->
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
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_02/ex02.py -->
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/day_02/ex03.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/day_02/ex03.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_02/ex03.py -->
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
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/day_02/ex03.py -->
<!-- MARKDOWN-AUTO-DOCS:END -->

