# Ex4: Flatten the following list to a new list:
countries = [[("Finland", "Helsinki")], [("Sweden", "Stockholm")], [("Norway", "Oslo")]]

# output:
# [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]

list = [
    [country.upper(), country[:3].upper(), capital.upper()]
    # In above line `country` and `capital` is from last line
    for list in countries
    for (country, capital) in list  # Here `list` is from above line
    # In above line we are destructuring tuple values
]
print(list)
