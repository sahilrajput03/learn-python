# Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries

from utils import readCountriesFromJsonFile

# TODO: ex2:Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries

countries = readCountriesFromJsonFile()
# print(countries)
# Output:
#  [{
#     "name": "Norway",
#     "capital": "Oslo",
#     "languages": [
#         "Norwegian",
#         "Norwegian Bokmål",
#         "Norwegian Nynorsk"
#     ],
#     "population": 5223256,
#     "flag": "https://restcountries.eu/data/nor.svg",
#     "currency": "Norwegian krone"
# }]
print("")


def most_populated_countries(countries, n=10):
    """Returns a list of the n most populated countries."""
    most_populated = sorted(
        countries, key=lambda country: country["population"], reverse=True
    )
    return most_populated[:n]


mostPopulartedCountries = most_populated_countries(countries, 10)
for mostPopulartedCountry in mostPopulartedCountries:
    print(mostPopulartedCountry["name"], mostPopulartedCountry["population"])

# Removing keys except "name" and "population" keys using List Comprehension
nameAndPopulationOfMostPopulatedCountries = [
    {
        "name": mostPopulartedCountry["name"],
        "population": mostPopulartedCountry["population"],
    }
    for mostPopulartedCountry in mostPopulartedCountries
]
for mostPopulartedCountry in nameAndPopulationOfMostPopulatedCountries:
    print(mostPopulartedCountry)
