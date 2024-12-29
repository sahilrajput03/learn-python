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
# 1. From Python 3.6 (2016) we use this `f-strings` syntax widely for their readability and efficiency
# when formatting strings.)
# 2. This approach is concise and more efficient compared to older methods like str.format() or string concatenation.


# Using str.format()                        (Way 2)
print(
    "{}, good to meet you!".format(x)
)  # You can use single ('') or double ("") quotes as you wish

# ###
# Note: Both methods (`f-strings` & `str.format`) allow you to include multiple variables in a string, but f-strings are generally preferred for their cleaner syntax.
# ###
