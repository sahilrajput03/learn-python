countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland"]
names = ["Asabeneh", "Lidiya", "Ermias", "Abraham"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Exercises: Level 1
#       Use for loop to print each country in the countries list.

# Use map to create a new list by changing each country to uppercase in the
#    countries list

uppercase_countries = map(lambda v: v.upper(), countries)
# print(uppercase_countries) # Prints address of the map object: <map object at 0x10ed60d30>
print(list(uppercase_countries))


# Use filter to filter out countries containing 'land'.
print(list(filter(lambda text: text.find("land") != -1, countries)))

# Use filter to filter out countries having exactly six characters.
print(list(filter(lambda country: len(country) == 6, countries)))
