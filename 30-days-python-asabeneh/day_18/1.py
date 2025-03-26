import re

# * A regular expression or RegEx is a special text string
#       that helps to find patterns in data. A RegEx can be used
#       to check if some pattern exists in a different data type.
#       To use RegEx in python first we should import the RegEx
#       module which is called re.

# * Methods in re Module
#   To find a pattern we use different set of re character sets that allows to search for a match in a string.
#       - re.match(): searches only in the beginning of the first line
#       of the string and returns matched objects if found, else
#       returns None.
#        - re.search: Returns a match object if there is
#           one anywhere in the string, including multiline strings.
#       - re.findall: Returns a list containing all matches
#       - re.split: Takes a string, splits it at the match points,
#           returns a list
#       - re.sub: Replaces one or many matches within a string

# & SYNTAX (re.I to ignore case)
# re.match(STRING_OR_PATTERN, INPUT_TEXT, re.I)

inputText = "I love to teach python and javaScript"
# It returns an object with span, and match
searchText = "I love to teach"
# print(len(searchText))  # 15

#  The match function returns an object only if the `txt` starts with the pattern
match = re.match(searchText, inputText, re.I)
print(match)  # <re.Match object; span=(0, 15), match='I love to teach'>

# * Using span() we get starting and ending position of the match as tuple
print(match.span())  # (0, 15)

# Destructure start and end from `span`
start, end = match.span()
print(start, end)  # 0, 15

# * awesome
substring = inputText[start:end]
print(substring)  # I love to teach

# inline way (looks a little dirty though)
print(inputText[match.span()[0] : match.span()[1]])  # I love to teach


# when searchText is not found in inputText
inputText = "I love to teach python and javaScript"
match = re.match("Baburaav ghr pe hai?", inputText, re.I)
print(match)  # None


print(" ---------------------------------")


# & re.search
# SYNTAX: re.search(STRING_OR_PATTERN, INPUT_TEXT, re.I)

# re.search is much better than re.match because it can look for the pattern
#       throughout the text. re.search returns a match object with a first
#       match that was found, otherwise it returns None.

inputText = """Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language"""

# It returns an object with span and match
match = re.search("first", inputText, re.I)
print(match)  # <re.Match object; span=(100, 105), match='first'>

# * Using span() we get starting and ending position of the match as tuple
span = match.span()
print(span)  # (100, 105)

# Lets find the start and stop position from the span
start, end = span
print(start, end)  # 100 105

substring = inputText[start:end]
print(substring)  # first


# & re.findall - Searching for *all* matches
matches = re.findall("language", inputText, re.I)
print(matches)  # ['language', 'language']

matches = re.findall("python", inputText, re.I)
print(matches)  # ['Python', 'python']

# Way 1 to search for python or Python without using re.I
matches = re.findall("Python|python", inputText)
print(matches)  # ['Python', 'python']

# Way 2 to search for python or Python without using re.I
matches = re.findall("[Pp]ython", inputText)
print(matches)  # ['Python', 'python']

# TODO: continue from - Replacing a Substring
