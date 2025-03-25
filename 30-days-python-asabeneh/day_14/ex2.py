from utils import readCountriesFromJsonFile

# * Ex. 13: Create a function returning a dictionary, where keys stand for starting
#   letters of countries and values are the number of country names starting
#   with that letter.

countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland"]


# & Learn: we get `KeyError: 'bad_key'` when we try to access key which is not defined in dictionary.
a = {"a": 20}
# print(a["badkey"])  # we get exception ---  `KeyError: 'bad_key'`


def get_first_letter_count(country_list):
    dictionary = {}
    for country in country_list:
        firstLetterOfCountry = country[0]
        # & Learn: We use `dictionary.get()` method because if we use dictionary["someBadKey"] then we get exception ---  `KeyError: 'bad_key'`
        dictionary[firstLetterOfCountry] = dictionary.get(firstLetterOfCountry, 0) + 1
    return dictionary


print(get_first_letter_count(countries))


countries = readCountriesFromJsonFile()

# Ex.14: Declare a get_first_ten_countries function - it returns a list of first
#       ten countries from the countries.js list in the data folder.
print(countries[:10])  # get_first_ten_countries

# Ex.15: Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
print(countries[-10:])  # get_last_ten_countries
