## \*\* operator in python

It's a bitwise XOR (exclusive OR).

exponential operator: \*\*

## Example: Multiline Comment

Triple quote can be used for multiline comment if it is not assigned to a variable

"""This is multiline comment multiline comment takes multiple lines. python is eating the world """

## Boolean types

Booleans A boolean data type is either a True or False value. T and F should be always uppercase.

Example:

```py
True  #  Is the light on? If it is on, then the value is True

False # Is the light on? If it is off, then the value is False
```

## List

Python list is an ordered collection which allows to store different data type items. A list is similar to an array in JavaScript.

Example:

[0, 1, 2, 3, 4, 5] # all are the same data types - a list of numbers ['Banana', 'Orange', 'Mango', 'Avocado'] # all the same data types - a list of strings (fruits!)
['Finland','Estonia', 'Sweden','Norway'] # all the same data types - a list of strings (countries!) ['Banana', 10, False, 9.81] # different data types in the list - string,
integer, boolean and float

## Dictionary

A python dictionary object is an unordered collection of data in a key:value pair format.

Example:

{'name':'Asabeneh', 'country':'Finland', age:250, 'is_married':True}

## Tuple

A tuple is an ordered collection of different data types like list but tuples can not be modified once they are created. They are immutable.

Example:

('Asabeneh', 'Brook', 'Abraham', 'Lidiya')

## Set

A set is a collection of data types similar to list and tuple. Unlike list and tuple, set is not an ordered collection of items. Like in mathematics, set in python stores only
unique items.

In later sections, we will go in detail about each and every python data type.

Example:

{3.14, 9.81, 2.7} # order is not important in set

## ordered vs. unordered

In ordered we can use index to access or manipulate the data simply.

## Simple builtin function

print(), len(), type(), int(), float(), str(), input(), list(), dict(), min(), max(), sum(), sorted(), open(), file(), help(), and dir().

## division things in python

```
print('Division: ', 7 / 2)
print('Division without the remainder: ', 7 // 2)   # gives without the floating number or without the remaining
```

## Example:Complex numbers

# Complex numbers

print('Complex number: ', 1+1j) print('Multiplying complex numbers: ',(1+1j) \* (1-1j))

## Example:Complex numbers

# Complex numbers

print('Complex number: ', 1+1j) print('Multiplying complex numbers: ',(1+1j) \* (1-1j))

## Logical Operators

and, or, not

## area of square

`area = pi * radius ** 2`

## array accessing from behind

If we want to start from right end we can use negative indexing. -1 is the last index.

```py
language = 'Python'
last_letter = language[-1]
print(last_letter) # n
second_last = language[-2]
print(second_last) # o

```

## Slicing strings

Slicing Python Strings In python we can slice strings into substrings.

language = 'Python' first_three = language[0:3] # starts at zero index and up to 3 but not include 3 last_three = language[3:6] print(last_three) # hon

- Another way

last_three = language[-3:] print(last_three) # hon last_three = language[3:] print(last_three) # hon

## Reversing a String

We can easily reverse strings in python.

greeting = 'Hello, World!' print(greeting[::-1]) # !dlroW ,olleH

## useful sring methods

- challenge.isalnum() - check for alpha numeric (Output: True or False)

- challenge.index(sub_string)
- challenge.find('y') # Returns the index number
- challenge.endswith('tion')
- challenge.capitalize()
- challenge.isdigit() # Output (True or False)

# join implementation in python

`'# '.join(web_tech)`

- title(): Returns a title cased string

```py
challenge = 'thirty days of python'
print(challenge.title()) # Thirty Days Of Python
```

- startswith(): Checks if String Starts with the Specified String

```py
challenge = 'thirty days of python'
print(challenge.startswith('thirty')) # True

challenge = '30 days of python'
print(challenge.startswith('thirty')) # False\
```

## Collection data types

- Ordered: List, Tuple
- Unordered: Set, Dictionary

## input

Default value in taken into string, we should conver to int or boolean or else as required.

## uppercase , lowercase string methods

`isupper(), islower(), lower(), upper()`

## closing 27 june, complete day4
