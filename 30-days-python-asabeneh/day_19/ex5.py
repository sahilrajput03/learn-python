import re
import os


# ex5. Find the most common words in the English language. Call the name of your function find_most_common_words, it will take two parameters - a string or a file and a positive integer, indicating the number of words. Your function will return an array of tuples in descending order. Check the output
def find_most_common_words(text, n):
    try:
        with open(text, "r") as f:
            content = f.read()
    except FileNotFoundError:
        content = text
    except OSError:
        # To capture `OSError: [Errno 63] File name too long:`
        content = text

    words = re.findall(r"\b\w+\b", content.lower())
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    sorted_word_counts = sorted(
        word_counts.items(), key=lambda item: item[1], reverse=True
    )
    return sorted_word_counts[:n]


print("\nBy providing filepath as argument:")
dirname = os.path.dirname(__file__)
data_file = os.path.join(dirname, "sample.txt")
[print(word) for word in find_most_common_words(data_file, 10)]

text = """
The Apollo 15 postal covers incident was a 1972 NASA scandal involving the astronauts of Apollo 15, who carried about 400 unauthorized postal covers (stamped and postmarked envelopes) into space and to the Moon's surface on the Lunar Module Falcon. Some of the envelopes were sold at high prices by West German stamp dealer Hermann Sieger, and are known as "Sieger covers". The crew of Apollo 15—David Scott, Alfred Worden, and James Irwin—agreed to take payments for carrying the covers; though they returned the money, they were reprimanded by NASA. Amid much press coverage of the incident, the astronauts were called before a closed session of a Senate committee and never flew in space again."""

print("\nBy providing text as argument:")
[print(word) for word in find_most_common_words(text, 10)]


print("----------------------")
# ex6. Use the function, find_most_frequent_words to find: a) The ten most frequent words used in Obama's speech b) The ten most frequent words used in Michelle's speech c) The ten most frequent words used in Trump's speech d) The ten most frequent words used in Melina's speech
print("\nObama Speech")
data_file = os.path.join(dirname, "..", "data", "obama_speech.txt")
[print(word) for word in find_most_common_words(data_file, 10)]

print("\nMischelle Speech")
data_file = os.path.join(dirname, "..", "data", "michelle_obama_speech.txt")
[print(word) for word in find_most_common_words(data_file, 10)]

print("\nDonald Trump Speech")
data_file = os.path.join(dirname, "..", "data", "donald_speech.txt")
[print(word) for word in find_most_common_words(data_file, 10)]

print("\nMelina Trump Speech")
data_file = os.path.join(dirname, "..", "data", "melina_trump_speech.txt")
[print(word) for word in find_most_common_words(data_file, 10)]
