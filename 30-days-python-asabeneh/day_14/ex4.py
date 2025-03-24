from utils import readCountriesFromJsonFile

# Level 3: Sort out the ten most populated countries
countries = readCountriesFromJsonFile()
sorted_countries = sorted(countries, key=lambda x: x["population"], reverse=True)

top_ten = sorted_countries[:10]
print("Ten most populated countries:")

for country in top_ten:
    print(f"{country['name']}: {country['population']:,} people")
