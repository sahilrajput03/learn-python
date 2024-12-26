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
