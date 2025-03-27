import re

# ex1: What is the most frequent word in the following paragraph?

paragraph = "I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love."

# Regex Explanation:
#   \W matches any non-word character (opposite of \w which matches [a-zA-Z0-9_])
#   + means "one or more occurrences"
words = re.split(r"\W+", paragraph.lower())
wordsCount = {}

for word in words:
    if word:  # Skip empty strings
        wordsCount[word] = wordsCount.get(word, 0) + 1

mostFrequentWord = max(wordsCount.items(), key=lambda x: x[1])
print(mostFrequentWord)
