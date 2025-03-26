import re

# & Replacing a Substring
# & =====================
inputText = """Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language"""

match_replaced = re.sub("Python|python", "JavaScript", inputText, re.I)
print(match_replaced)
# Output: JavaScript is the most beautiful language that a human being has ever created. I recommend JavaScript for a first programming language

# OR

match_replaced = re.sub("[Pp]ython", "JavaScript", inputText, re.I)
print(match_replaced)
# Output: JavaScript is the most beautiful language that a human being has ever created. I recommend JavaScript for a first programming language


print("-----------------------")

inputText = """%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?"""

matches = re.sub("%", "", inputText)
print(matches)
# Output:
# I am teacher and  I love teaching.
# There is nothing as rewarding as educating and empowering people.
# I found teaching more interesting than any other jobs.
# Does this motivate you to be a teacher?


print("-----------------------")

inputText = """I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?"""

print(re.split("\n", inputText))  # splitting using \n - end of line symbol
# Output:
# [
#     "I am teacher and  I love teaching.",
#     "There is nothing as rewarding as educating and empowering people.",
#     "I found teaching more interesting than any other jobs.",
#     "Does this motivate you to be a teacher?",
# ]

# & Writing RegEx Patterns
regexPattern = r"apple"
inputText = "Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. "

matches = re.findall(regexPattern, inputText)
print(matches)  # ['apple']

# case insensitive search
matches = re.findall(regexPattern, inputText, re.I)
print(matches)  # ['Apple', 'apple']

# Or we can use a set of characters method i.e, [Aa]  --- this mean the first letter could be A or a
regexPattern = r"[Aa]pple"
matches = re.findall(regexPattern, inputText)
print(matches)  # ['Apple', 'apple']

# & Writing RegEx Patterns
# & ======================

# []: A set of characters
#   [a-c] means, a or b or c
#   [a-z] means, any letter from a to z
#   [A-Z] means, any character from A to Z
#   [0-3] means, 0 or 1 or 2 or 3
#   [0-9] means any number from 0 to 9
#   [A-Za-z0-9] any single character, that is a to z, A to Z or 0 to 9
# \: uses to escape special characters
#   \d means: match where the string contains digits (numbers from 0-9)
#   \D means: match where the string does not contain digits
# . : any character except new line character(\n)
# ^: starts with
#   r'^substring' eg r'^love', a sentence that starts with a word love
#   r'[^abc] means not a, not b, not c.
# $: ends with
#   r'substring$' eg r'love$', sentence that ends with a word love
# *: zero or more times
#   r'[a]*' means a optional or it can occur many times.
# +: one or more times
#   r'[a]+' means at least once (or more)
# ?: zero or one time
#   r'[a]?' means zero times or once
# {3}: Exactly 3 characters
# {3,}: At least 3 characters
# {3,8}: 3 to 8 characters
# |: Either or
#   r'apple|banana' means either apple or a banana
# (): Capture and group

# 🛑🛑🛑🛑🛑🛑🛑🛑 TODO: add below image just below this file's code in readme.
# ![](./30-days-python-asabeneh/images/regex-chart.png)
# 🛑🛑🛑🛑🛑🛑🛑🛑🛑

# & Square Bracket
regexPattern = r"[Aa]pple"  # this square bracket mean either A or a
matches = re.findall(regexPattern, inputText)
print(matches)  # ['Apple', 'apple']

# Using square brackets and or (|) operator - we extract Apple, apple, Banana, banana
regexPattern = r"[Aa]pple|[Bb]anana"
inputText = "Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away."
matches = re.findall(regexPattern, inputText)
print(matches)  # ['Apple', 'banana', 'apple', 'banana']


# & Escape character(\)
regexPattern = r"\d"  # d is a special character which means digits
inputText = "This regular expression example was made on December 6,  2019 and revised on July 8, 2021"
matches = re.findall(regexPattern, inputText)
print(matches)
# ['6', '2', '0', '1', '9', '8', '2', '0', '2', '1']

# & One or more times(+)
# d is a special character which means digits, + mean one or more times
regexPattern = r"\d+"
inputText = "This regular expression example was made on December 6,  2019 and revised on July 8, 2021"
matches = re.findall(regexPattern, inputText)
print(matches)  # ['6', '2019', '8', '2021'] - now, this is better!

print("------------------------------ ")

# & Period(.) - Any character except new line character
inputText = """Apple and banana are fruits"""
# The square bracket means a and . means any character except new line
regexPattern = r"[a]."
matches = re.findall(regexPattern, inputText)
print(matches)  # ['an', 'an', 'an', 'a ', 'ar'] # ✅

# . means any character except new line character, + means any character one or more times
regexPattern = r"[a].+"
matches = re.findall(regexPattern, inputText)
print(matches)  # ['and banana are fruits'] # ✅✅


# & Asterisk(*) - Any character ZERO or MORE TIMES
# . means any character, * any character zero or more times
regexPattern = r"[a].*"
inputText = """Apple and banana are fruits"""
matches = re.findall(regexPattern, inputText)
print(matches)  # ['and banana are fruits'] # ✅

# & (?) - Any character ZERO or ONE TIME
# Zero or one time. The pattern may not occur or it may occur once.

inputText = """I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail."""
regexPattern = r"[Ee]-?mail"  # ? means here that '-' is optional
matches = re.findall(regexPattern, inputText)
print(matches)  # ['e-mail', 'email', 'Email', 'E-mail'] # ✅

# & Quantifier ({})
# We can specify the length of the substring we are looking for in a
#       text, using a curly bracket. Let us imagine, we are interested in a
#       substring with a length of 4 characters:
inputText = "This regular expression example was made on December 6,  2019 and revised on July 8, 2021"
regexPattern = r"\d{4}"  # exactly four times
matches = re.findall(regexPattern, inputText)
print(matches)  # ['2019', '2021']

inputText = "This regular expression example was made on December 6,  2019 and revised on July 8, 2021"
regexPattern = r"\d{1, 4}"  # 1 to 4
matches = re.findall(regexPattern, inputText)
print(matches)  # ['6', '2019', '8', '2021']


# & Cart ^ (❤️)
#  1. Starts with
inputText = "This regular expression example was made on December 6,  2019 and revised on July 8, 2021"
regexPattern = r"^This"  # ^ means starts with
matches = re.findall(regexPattern, inputText)
print(matches)  # ['This']

# 2. Negation
txt = "This regular expression example was made on December 6,  2019 and revised on July 8, 2021"
regex_pattern = r"[^A-Za-z ]+"  # ^ in set character means negation, not A to Z, not a to z, no space
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6,', '2019', '8', '2021']
