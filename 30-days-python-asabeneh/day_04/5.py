# join(): Returns a concatenated string
web_tech = ["HTML", "CSS", "JavaScript", "React"]
result = ", ".join(web_tech)
print(result)  # 'HTML, CSS, JavaScript, React'
print()


# strip(): Removes all given characters starting from the beginning and end of the string
print("strip()")
print(" Thirty days of python ")
# Removes leading and trailing white space character
print(" Thirty days of python ".strip())
print("thirty days of pythonBATMAN".strip("BATMAN"))  # "thirty days of python"
print()


# replace(): Replaces substring inside
challenge = "thirty days of python"
print(challenge.replace("python", "coding"))  # 'thirty days of coding'

# split():Splits String from Left
challenge = "thirty days of python"
print(challenge.split())  # ['thirty', 'days', 'of', 'python']
challenge = "thirty, days, of, python"
print(challenge.split(", "))  # ['thirty', 'days', 'of', 'python']

# title(): Returns a Title Cased String
challenge = "thirty days of python"
print(challenge.title())  # Thirty Days Of Python
print()

# swapcase(): Checks if String Starts with the Specified String
"""
The swapcase() method returns a new string where all the case swapping rules below are applied:

Uppercase characters are converted to lowercase
Lowercase characters are converted to uppercase
All other characters remain unchanged
"""
challenge = "thirty days of python"
print(challenge.swapcase())  # THIRTY DAYS OF PYTHON
challenge = "Thirty Days Of Python"
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON

# startswith(): Checks if String Starts with the Specified String
challenge = "thirty days of python"
print(challenge.startswith("thirty"))  # True
challenge = "30 days of python"
print(challenge.startswith("thirty"))  # False
