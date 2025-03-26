import re

# Clean the following text. After cleaning, count three most frequent
#       words in the string.
sentence = """%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?"""
# Clean the text using regex to remove special characters
clean_sentence = re.sub(r"[%$@#&;!?,.]", "", sentence)

# From exercise
expectedSentence = "I am a teacher and I love teaching There is nothing as more rewarding as educating and empowering people I found teaching more interesting than any other jobs Does this motivate you to be a teacher"
if clean_sentence == expectedSentence:
    print("Sentence cleaning successful ✅")
else:
    print("Sentence cleaning FAILED 🛑")

# Split into words and count frequencies
words = clean_sentence.split()
wordsCount = {}
for word in words:
    wordsCount[word] = wordsCount.get(word, 0) + 1

# Get 3 most frequent words
mostCountWord = sorted(wordsCount.items(), key=lambda x: x[1], reverse=True)[:3]
print("Most frequent words:", mostCountWord)
