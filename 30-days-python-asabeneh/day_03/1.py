# source of this file:
# https://github.com/Asabeneh/30-Days-Of-Python/blob/master/03_Day_Operators/day-3.py
# Note to Sahil: I have kept only non-repetitive code in this file from above
# reference file.

print("Multiplying complex number: ", (1 + 1j) * (1 - 1j))

print(3 > 2)  # True, because 3 is greater than 2
print(3 >= 2)  # True, because 3 is greater than 2
print(3 < 2)  # False,  because 3 is greater than 2
print(2 < 3)  # True, because 2 is less than 3
print(2 <= 3)  # True, because 2 is less than 3
print(3 == 2)  # False, because 3 is not equal to 2
print(3 != 2)  # True, because 3 is not equal to 2
print(len("mango") == len("avocado"))  # False
print(len("mango") != len("avocado"))  # True
print(len("mango") < len("avocado"))  # True
print(len("milk") != len("meat"))  # False
print(len("milk") == len("meat"))  # True
print(len("tomato") == len("potato"))  # True
print(len("python") > len("dragon"))  # False

# Boolean comparison
print("True == True: ", True == True)  # True
print("True == False: ", True == False)  # False
print("False == False:", False == False)  # True
print("True and True: ", True and True)  # True
print("True or False:", True or False)  # True


# Another way comparison
# ======================
# print("1 is 1", 1 is 1)  # True - because the data values are the same
# print("1 is not 2", 1 is not 2)  # True - because 1 is not 2
# print("4 is 2 ** 2:", 4 is 2**2)  # True
"""
* Sahil: Above three statements throws syntax warning because it isn't recommended approach.
* We get this warning -
`SyntaxWarning: "is" with a literal. Did you mean "=="?`

The is operator should primarily be used for:
1. Comparing with None
2 Identity comparison when you specifically need to check if two variables reference the same object
"""

print("A in Asabeneh", "A" in "Asabeneh")  # True - A found in the string
print("B in Asabeneh", "B" in "Asabeneh")  # False -there is no uppercase B
print("coding" in "coding for all")  # True - because coding for all has the word coding
print("coding" not in "coding for all")  # False
print("xyz" not in "coding for all")  # True
print("a in an:", "a" in "an")  # True
print(3 > 2 and 4 > 3)  # True - because both statements are true
print(3 > 2 and 4 < 3)  # False - because the second statement is false
print(3 < 2 and 4 < 3)  # False - because both statements are false
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statement is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print(not 3 > 2)  # False - because 3 > 2 is true, then not True gives False
print(not True)  # False - Negation, the not operator turns true to false
print(not False)  # True
print(not not True)  # True
print(not not False)  # False
