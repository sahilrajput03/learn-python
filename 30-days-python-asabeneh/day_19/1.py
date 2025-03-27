# & File Handling
# * Syntax:
# open("filename", mode)
# where `mode` can be r, a, w, x, t, b  could be to read, write, update.
# * "r" - Read - Default value. Opens a file for reading, it returns an error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# * "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

import os

dirname = os.path.dirname(__file__)
filePath = os.path.join(dirname, "reading_file_example.txt")

f = open(filePath)
# print(f) # Output: <_io.TextIOWrapper name='./files/reading_file_example.txt' mode='r' encoding='UTF-8'>
txt = f.read()  # <class 'str'>
f.close()  # An opened file has to be closed with close() method.

print(type(txt))
print(txt)
# Output:
"""
This is an example to show how to open a file and read.
This is the second line of the text.
"""

# * Instead of printing all the text, let us print the first 10 characters of the text file.
f = open(filePath)
txt = f.read(10)
print(txt)  # Output: This is an
f.close()


# * readline(): read only the first line
f = open(filePath)
line = f.readline()
print(line)  # This is an example to show how to open a file and read.
f.close()

# * readlines(): read all the text line by line and returns a list of lines
f = open(filePath)
lines = f.readlines()
f.close()
print(type(lines))  # # <class 'list'>
print(lines)  #
[
    "This is an example to show how to open a file and read.\n",
    "This is the second line of the text.",
]

# * splitlines(): To get all the lines as a list
f = open(filePath)
lines = f.read().splitlines()
f.close()
print(type(lines))  # <class 'list'>
print(lines)
# ['This is an example to show how to open a file and read.', 'This is the second line of the text.']

print("------------------------------")

# & After we open a file, we should close it. There is a high tendency of forgetting to close them. There is a new way of opening files using with - closes the files by itself. Let us rewrite the the previous example with the with method:
with open(filePath) as f:
    lines = f.read().splitlines()
    print(type(lines))  # <class 'list'>
    print(lines)
    # ['This is an example to show how to open a file and read.', 'This is the second line of the text.']


# & Opening Files for Writing and Updating
# To write to an existing file, we must add a mode as parameter to the open() function:

# "a" - append - will append to the end of the file, if the file does not it creates a new file.
# "w" - write - will overwrite any existing content, if the file does not exist it creates.

# * Let us append some text to the file we have been reading:
filePath = os.path.join(dirname, "file2.txt")  # & Using `file2.txt` now
with open(filePath, "a") as f:
    f.write("This text has to be appended at the end. ")

# * The method below creates a new file, if the file does not exist:
filePath = os.path.join(dirname, "file3.txt")  # & Using `file2.txt` now
with open(filePath, "w") as f:
    f.write("This text will be written in a newly created file")


# * Deleting Files
filePath = os.path.join(dirname, "NON_EXISTING_FILE.txt")  # & Using `file2.txt` now
# If the file does not exist, the remove() method will raise an error `FileNotFoundError`,
#       so it is good to use a condition like this:
if os.path.exists(filePath):
    os.remove(filePath)
else:
    print("The file does not exist")
