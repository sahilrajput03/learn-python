# case 4,7

pseduo code

```py
m = 1, f =1

mNeeded = 4-1 = 3
fNeeded = 7-1 = 6

-
if mNeeded > 0:
    fToReplicate = mNeeded if mNeeded <= f else f
    # for instance say `f=5` and `mNeeded=3` so we set fToReplicate=3.
    m = m + fToReplicate


```

## LEARNING PYTHON:

1. You can edit a global variable in python very easily:

```py
total = 100
def func():
    # refer to global variable 'total' inside function
    global total
    if total > 10:
        total = 15
print('Total = ', total) # 100
func()
print('Total = ', total) # 15
```

Refer below link for more.
https://thispointer.com/python-how-to-use-global-variables-in-a-function/

below is shit..
Passing param and checking if reference value can be changed.

```py
a = 10
print('initial', a)

def main(x):
    a=15
    x=15
    print('--scoped-a',a)
    print('--scoped-x',x)

main(a)
print('unscoped',a)
```

Ouput:

```
initial 10
--scoped-a 15
--scoped-x 15
unscoped 10
```

Amazing: Strings are immutable when we pass the value as param to any function in python. So beware of it. Read more at amazing text @ link below.
https://stackoverflow.com/a/986145

The best way we can do what we want is by returning the value it its own from the function itself, i.e.,
`val1 = my_function(val1)`
and that'll work absolutely fine.

2. ternary operator in python

```py
# Program to demonstrate conditional operator
a, b = 10, 20

# Copy value of a in min if a < b else copy b
min = a if a < b else b

print(min)
```
