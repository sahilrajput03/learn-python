# source of this and following files in this day --
# https://github.com/Asabeneh/30-Days-Of-Python/blob/master/04_Day_Strings/day_4.py

# Single line comment
letter = "P"  # A string could be a single character or a bunch of texts
print(letter)  # P
print(len(letter))  # 1

greeting = "Hello, World!"  # String could be  a single or double quote,"Hello, World!"
print(greeting)  # Hello, World!
print(len(greeting))  # 13

sentence = "I hope you are enjoying 30 days of python challenge"
print(sentence)
print()

# Multiline String
multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)
print()

# Another way of doing the same thing
multiline_string = "I am a teacher and enjoy teaching.\nI didn't find anything as rewarding as empowering people.\nThat is why I created 30 days of python."
print(multiline_string)
print()


lines = [
    "I am a teacher and enjoy teaching.",
    "I didn't find anything as rewarding as empowering people.",
    "That is why I created 30 days of python.",
]
"\n".join(lines)
print(lines)
