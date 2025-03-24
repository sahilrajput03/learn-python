# Flatten the following list to a new list:
countries = [[("Finland", "Helsinki")], [("Sweden", "Stockholm")], [("Norway", "Oslo")]]

# output:
# [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]

list = [
    [tuple[0].upper(), tuple[0][:3].upper(), tuple[1].upper()]
    # #  Above line `tuple` is from the last line
    for list in countries
    for tuple in list  # Here `list` is from above line
]
print(list)
