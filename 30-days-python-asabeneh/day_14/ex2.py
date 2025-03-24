import json
import os

# * Ex. 13: Create a function returning a dictionary, where keys stand for starting
#   letters of countries and values are the number of country names starting
#   with that letter.

countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland"]


def get_first_letter_count(country_list):
    letter_count = {}
    for country in country_list:
        first_letter = country[0]
        letter_count[first_letter] = letter_count.get(first_letter, 0) + 1
    return letter_count


print(get_first_letter_count(countries))


# * Prompt to Copilot for reading json file:
# Read file `countries_data.json` from `data` folder which is present in
#       parent folder of current script.
def readCountriesFromJsonFile():
    dirname = os.path.dirname(os.path.dirname(__file__))
    data_file = os.path.join(dirname, "data", "countries_data.json")

    with open(data_file, "r") as f:
        countries_data = json.load(f)
    return countries_data


countries = readCountriesFromJsonFile()

# Ex.14: Declare a get_first_ten_countries function - it returns a list of first
#       ten countries from the countries.js list in the data folder.
print(countries[:10])  # get_first_ten_countries

# Ex.15: Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
print(countries[-10:])  # get_last_ten_countries
