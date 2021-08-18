# Amazing answer on using list comprehensions in python : https://stackoverflow.com/a/4260304

# This file teaches you to execute things in simple ternary operators.
a = 1
b = 1
c = 1

def setA(a):
    a = 10

def setB(b):
    b = 10


setA(a) if (c == 3) else setB(b)
print(b)