# ex9. Read the hacker news csv file and find out:
#       a) Count the number of lines containing python or Python
#       b) Count the number lines containing JavaScript, javascript or Javascript
#       c) Count the number lines containing Java and not JavaScript
from utils import readTextFileFromUrl

hackerNewsCsvFileUrl = "https://raw.githubusercontent.com/Asabeneh/30-Days-Of-Python/refs/heads/master/data/hacker_news.csv"
fileContent = readTextFileFromUrl(hackerNewsCsvFileUrl)


def countLines(keyword):
    """Counts the number of lines in a file at a URL containing a keyword."""
    lines = fileContent.splitlines()
    count = 0
    for line in lines:
        if keyword in line:
            count += 1
    return count


def countLinesWithExclusion(keyword, exclude_keyword):
    """Counts lines containing a keyword but not another keyword."""
    lines = fileContent.splitlines()
    count = 0
    for line in lines:
        if keyword in line and exclude_keyword not in line:
            count += 1
    return count


# a) Count lines containing python or Python
python_count = countLines("python") + countLines("Python")
print(f"Number of lines containing Python or python: {python_count}")

# b) Count lines containing JavaScript, javascript or Javascript
javascript_count = (
    countLines("JavaScript") + countLines("javascript") + countLines("Javascript")
)

print(
    f"Number of lines containing JavaScript, javascript, or Javascript: {javascript_count}"
)

# c) Count lines containing Java and not JavaScript
java_count = countLinesWithExclusion("Java", "JavaScript")
print(f"Number of lines containing Java and not JavaScript: {java_count}")
