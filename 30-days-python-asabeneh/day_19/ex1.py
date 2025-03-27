# ex1: Write a function which count number of lines and number of words in a text. All the files are in the data the folder: a) Read obama_speech.txt file and count number of lines and words.

import os
import re

dirname = os.path.dirname(__file__)
filePath = os.path.join(dirname, "..", "data", "obama_speech.txt")

with open(filePath) as f:
    lines = f.readlines()
    print(len(lines))  # 66


with open(filePath) as f:
    txt = f.read()
    # Regex Explanation:
    #   \W matches any non-word character (opposite of \w which matches [a-zA-Z0-9_])
    #   + means "one or more occurrences"
    words = re.split(r"\W+", txt.lower())
    print(len(words))  # 2402
