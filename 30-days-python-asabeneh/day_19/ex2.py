from utils import readCountriesFromJsonFile

# ex2: Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages

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


def most_spoken_languages(countries, n):
    languages = {}
    for country in countries:
        for language in country["languages"]:
            if language in languages:
                languages[language] += 1
            else:
                languages[language] = 1
    # print(languages.items()) # dict_items([('Pashto', 1), ('Uzbek', 2),..])
    # print(type(languages.items())) # <class 'dict_items'>
    sorted_languages = sorted(languages.items(), key=lambda x: x[1], reverse=True)
    return sorted_languages[:n]
    # return sorted_languages[-10:] # (Get least spoken languages)


mostSpokenLanguages = most_spoken_languages(countries, 10)
for mostSpokenLanguage in mostSpokenLanguages:
    print(mostSpokenLanguage)
