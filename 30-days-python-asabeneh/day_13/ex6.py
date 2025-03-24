# Ex6: Change the following list of lists to a list of concatenated strings:
names = [
    [("Asabeneh", "Yetayeh")],
    [("David", "Smith")],
    [("Donald", "Trump")],
    [("Bill", "Gates")],
]
# Output:
# ["Asabeneh Yetaeyeh", "David Smith", "Donald Trump", "Bill Gates"]

list = [
    firstname + " " + lastname
    # Above line `firstname` and `lastname` is from the last line
    for list in names
    for (firstname, lastname) in list  # Here `list` is from above line
]
print(list)
