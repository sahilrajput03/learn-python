from utils import readCountriesFromJsonFile

# Level 3: Sort countries by name, by capital, by population
countries = readCountriesFromJsonFile()
sorted_by_name = sorted(countries, key=lambda x: x["name"])
sorted_by_capital = sorted(countries, key=lambda x: x.get("capital", ""))
sorted_by_population = sorted(countries, key=lambda x: x.get("population", 0))

print("Countries sorted by name:")
print([country["name"] for country in sorted_by_name[:5]])

print("\nCountries sorted by capital:")
print([country["name"] for country in sorted_by_capital[:5]])

print("\nCountries sorted by population:")
print([country["name"] for country in sorted_by_population[:10]])
