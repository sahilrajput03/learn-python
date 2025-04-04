# Check if type of '10' is equal to type of 10
a = "10"
b = 10
print(type(a) == type(b))  # False

try:
    # Check if int('9.8') is equal to 10
    # This statement throws runtime error: `ValueError: invalid literal for
    # int() with base 10: '9.8'``
    c = int("9.8")
except ValueError:
    print("Got ValueError")  # Got ValueError
else:
    print("No exceptions occurred.")
