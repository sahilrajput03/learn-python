# Ex5: Change the following list to a list of dictionaries:
countries = [[("Finland", "Helsinki")], [("Sweden", "Stockholm")], [("Norway", "Oslo")]]
# Output:
# [{'country': 'FINLAND', 'city': 'HELSINKI'},
# {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
# {'country': 'NORWAY', 'city': 'OSLO'}]

list = [
    [{"country": country.upper(), "city": capital.upper()}]
    # #  Above line `tuple` is from the last line
    for list in countries
    for (country, capital) in list  # Here `list` is from above line
]
print(list)
