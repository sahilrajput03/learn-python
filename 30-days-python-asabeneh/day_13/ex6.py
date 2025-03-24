# Change the following list of lists to a list of concatenated strings:
names = [
    [("Asabeneh", "Yetayeh")],
    [("David", "Smith")],
    [("Donald", "Trump")],
    [("Bill", "Gates")],
]
# Output:
# ["Asabeneh Yetaeyeh", "David Smith", "Donald Trump", "Bill Gates"]

list = [
    tuple[0] + " " + tuple[1]
    # Above line `tuple` is from the last line
    for list in names
    for tuple in list  # Here `list` is from above line
]
print(list)
