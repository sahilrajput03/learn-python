from functools import reduce

countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland"]
names = ["Asabeneh", "Lidiya", "Ermias", "Abraham"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Ex. Use map to create a new list by changing each country to uppercase in the
#    countries list

uppercase_countries = map(lambda v: v.upper(), countries)
# print(uppercase_countries) # Prints address of the map object: <map object at 0x10ed60d30>
print(list(uppercase_countries))


# Ex. Use filter to filter out countries containing 'land'.
print(list(filter(lambda text: text.find("land") != -1, countries)))

# Ex. Use filter to filter out countries having exactly six characters.
print(list(filter(lambda country: len(country) == 6, countries)))

# Ex. Use filter to filter out countries containing six letters and more in the country list.
print(list(filter(lambda country: len(country) > 6, countries)))

# Ex. Use filter to filter out countries starting with an 'E'
print(list(filter(lambda country: country.startswith("E"), countries)))


# Ex. Declare a function called get_string_lists which takes a list as a
# parameter and then returns a list containing only string items.
def get_string_lists(list1):
    return list(filter(lambda x: type(x) == str, list1))


list1 = ["1", 2, 3, "4", 5, "6"]
print(get_string_lists(list1))  # Output: ["1", "4", "6"]


# Ex. Use reduce to concatenate all the countries and to produce this sentence:
#       Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European
#       countries


def joinCountriesProperly(accumulator, current):
    isLastElement = current == countries[-1]
    if isLastElement:
        return accumulator + ", and " + current
    return accumulator + ", " + current


print(reduce(joinCountriesProperly, countries) + " are north European countries")
