_See older readme: [Click here](./README.old.md) (README.old.md)_

# 30 Days of Python

Code generate via autodocs

## File - `30-days-python-asabeneh/1.1.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/1.1.py) -->
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/1.2.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/1.2.py) -->
<!-- MARKDOWN-AUTO-DOCS:END -->


## File - `30-days-python-asabeneh/2.1.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/2.1.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/2.1.py -->
```py
x = input('Please enter your name\n')
print(f"{x} , good to meet you!")
# f means formatted string, cool.!
# From python 3 we use mordern syntax.
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/2.2.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/2.2.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/2.2.py -->
```py
s = 'sahil'
print(len(s))
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/2.3.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/2.3.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/2.3.py -->
```py
a = 4
b = 3
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')
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
pto = language[0,6:2] #
print(pto) # Pto
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/2.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/2.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/2.py -->
```py
x = input('Please enter your name\n')
print(x + ', good to meet you!')
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/3-game.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/3-game.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/3-game.py -->
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

## File - `30-days-python-asabeneh/3.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/3.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/3.py -->
```py
# Nested list comprehension example.
# I stands for input from user.
x = int(input('Enter x\n'))
y = int(input('Enter y\n'))
z = int(input('Enter z\n'))
n = int(input('Enter n\n'))

myLambda = lambda a, b, c, d: a + b + c != d # this prints True or False.

X = range(x) # X [0, 1, 2 , ...x-1]
Y = range(y)
Z = range(z)
N = range(n)

# PRINTS ALL THE POINTS IN SPACE.
# points = [[xval, yval, zval] for xval in X for yval in Y for zval in Z] # Prints all the points.

# SOLUTION BELOW:
points = [[xval, yval, zval] for xval in X for yval in Y for zval in Z if myLambda(xval, yval, zval, n)] # SOLUTION USING LAMBDA FUNCTION.
# points = [[xval, yval, zval] for xval in X for yval in Y for zval in Z if xval+yval+zval != n] # SIMPLE SOLUTION.

print(points)
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## File - `30-days-python-asabeneh/4-s.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/4-s.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/4-s.py -->
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

## File - `30-days-python-asabeneh/5-game.py`

<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./30-days-python-asabeneh/5-game.py) -->
<!-- The below code snippet is automatically added from ./30-days-python-asabeneh/5-game.py -->
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
