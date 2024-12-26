_See older readme: [Click here](./README.old.md) (README.old.md)_

# 30 Days of Python

Code generate via autodocs

## File - `30-days-python-asabeneh/1.1.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/1.1.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/1.1.py -->
```py
# Day 1 - 30DaysOfPython Challenge

print(2 + 3)                     # addition(+)
print(3 - 1)                     # subtraction(-)
print(2 * 3)                     # multiplication(*)
print(3 / 2)                     # division(/)
print(3 ** 2)                    # exponential(**)
print(3 % 2)                     # modulus(%)
print(3 // 2)                    # Floor division operator(//)
print()

# Checking data types
print(type(10))                  # <class 'int'>
print(type(3.14))                # <class 'float'>
print(type(1 + 3j))              # <class 'complex'>
print(type('Asabeneh'))          # <class 'str'>
print(type([1, 2, 3]))           # Li<class 'list'>st   
print(type({'name':'Asabeneh'})) # <class 'dict'>
print(type({9.8, 3.14, 2.7}))    # <class 'set'>
print(type((9.8, 3.14, 2.7)))    # <class 'tuple'>
print()
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/1.2.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/1.2.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/1.2.py -->
```py
# All below if statements resolve to true.

#### Using `type` function
if type(10) == int:
    print("integer type")

if type(3.14) == float:
    print("float type")

if type(1 + 3j) == complex:
    print("complex type")

if type('Asabeneh') == str:
    print("str type")

if type([1,2,3]) == list:
    print("list type")

if type({9.8, 3.14, 2.7}) == set:
    print("set type")

if type((9.8, 3.14, 2.7)) == tuple:
    print("tuple type")
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

if type('Asabeneh') == str:
    print("str type")

if isinstance([1,2,3], list):
    print("list type")

if isinstance({9.8, 3.14, 2.7}, set):
    print("set type")

if isinstance((9.8, 3.14, 2.7), tuple):
    print("tuple type")
print()
```
<!-- MARKDOWN-AUTO-DOCS:END -->


## File - `30-days-python-asabeneh/2.1.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/2.1.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/2.1.py -->
```py
# Printing variables
# #########################

x = input('Please enter your name\n')

if type(x) == str:
    print("str type")

# f-strings (formatted string literals)     (Way 1)
print(f"{x}, good to meet you!")
# Note:
# 1. From Python 3.6 (2016) we use this `f-strings` syntax widely for their readability and efficiency
# when formatting strings.)
# 2. This approach is concise and more efficient compared to older methods like str.format() or string concatenation.


# Using str.format()                        (Way 2)
print("{}, good to meet you!".format(x))

# ###
# Note: Both methods (`f-strings` & `str.format`) allow you to include multiple variables in a string, but f-strings are generally preferred for their cleaner syntax.
# ###
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/2.2.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/2.2.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/2.2.py -->
```py
s = 'sahil'
print(len(s)) # 5

if len(s) == 5:
    print('Yes it is a 5.')
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/2.3.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/2.3.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/2.3.py -->
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

## File - `30-days-python-asabeneh/2.4.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/2.4.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/2.4.py -->
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

## File - `30-days-python-asabeneh/2.5.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/2.5.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/2.5.py -->
```py
language = 'Python'
pto = language[0:6:2] #
print(pto)              # "Pto"
print(type(pto) == str) # True
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/3.1.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/3.1.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/3.1.py -->
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

## File - `30-days-python-asabeneh/3.2.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/3.2.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/3.2.py -->
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
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/4.1.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/4.1.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/4.1.py -->
```py
# Get no. of user.
# max no. of attempt 3.

target = 7 # right no.

count = 1

def game(count):
  i = int(input('Try your luck, choose a number..\n'))
  count += 1
  if i == target:
    print('Hooray..!')
  else:
    if count > 3:
      print('Sorry, You loose!!')
      return
      # ^^ terminate the function execution.
    game(count)

# start the game...
game(count)
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/5.1.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/5.1.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/5.1.py -->
```py
print("""🤠︎ Welcome to the game
Infomation:
Start - to start the car
stop - to stop the car
quit - to exit
help - car manual""")

info = """Start - to start the car
stop - to stop the car
quit - to exit

CASE: If user types any wrong choice..!
print >>> I don't understand that...

CASE: If choose start
Car started...Ready to go!

CASE: If choose stop
Car stopped."""
isCarStarted = False

def game(isCarStarted):
  choice = input().lower()
  if choice == 'help':
    print(info)
    game(isCarStarted)
  elif choice == 'start':
    if isCarStarted == True:
      print('You car is already started🥶︎!')
      game(isCarStarted)
    print('Your car started..🚀︎🚀︎!!.')
    isCarStarted = True
    game(isCarStarted)
  elif choice == 'stop':
    if isCarStarted == False:
      print('You car is already stopped🥶︎!')
      game(isCarStarted)
    print('You car stopped ..🛑︎🛑︎')
    isCarStarted = False
    game(isCarStarted)
  elif choice == 'quit':
    print('Thanks for playing the game 🧸︎')
    return
  else:
    print("I don't understand that...")
    print('Try again..')
    game(isCarStarted)

game(isCarStarted)
```
<!-- MARKDOWN-AUTO-DOCS:END -->
