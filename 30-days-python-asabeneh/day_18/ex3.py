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
