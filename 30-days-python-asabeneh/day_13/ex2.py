# Ex2: Flatten the following list of lists of lists to a one dimensional list :
y = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
# Expected output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

list = [
    item  # Here `item` is from last line
    for nestedList in y
    for subNestedList in nestedList  # Here `nestedList` is from above line
    for item in subNestedList  # Here `subNestedList` is from above line
]
print(list)
