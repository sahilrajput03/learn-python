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
