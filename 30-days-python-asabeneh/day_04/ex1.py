# 9. Cut(slice) out the first word of 'Coding For All' string.
string = "Coding For All"
print(string.split(" ")[0])

"""
10. Check if "Coding For All" string contains a word "Coding" using the method:
- index
- find or other methods.
"""
word = "Coding"

try:
    # Note: If `word` is not found in `string below statement throws runtime error (`ValueError: substring not found`)
    indexOfWord = string.index(word)
except ValueError:
    print("Got ValueError")
else:
    print("No exceptions occurred.")  # "No exceptions occurred."


print(type(indexOfWord) == int)  # True


indexOfWord = string.find(word) != -1
print(indexOfWord)  # True

# 18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
string1 = "Python For Everyone"
list = string1.split()
acronym = list[0][0] + list[1][0] + list[2][0]
print(acronym)
