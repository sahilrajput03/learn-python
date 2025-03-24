# Change the following list to a list of dictionaries:
countries = [[("Finland", "Helsinki")], [("Sweden", "Stockholm")], [("Norway", "Oslo")]]
# Output:
# [{'country': 'FINLAND', 'city': 'HELSINKI'},
# {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
# {'country': 'NORWAY', 'city': 'OSLO'}]

list = [
    [{"country": tuple[0].upper(), "city": tuple[1].upper()}]
    # #  Above line `tuple` is from the last line
    for list in countries
    for tuple in list  # Here `list` is from above line
]
print(list)
