from utils import readCountriesFromJsonFile

# Level 3: Sort countries by name, by capital, by population
countries = readCountriesFromJsonFile()
sorted_by_name = sorted(countries, key=lambda x: x["name"])
# sorted_by_capital = sorted(countries, key=lambda x: x.get("capital", ""))
# sorted_by_population = sorted(countries, key=lambda x: x.get("population", 0))

print("Countries sorted by name:", [c["name"] for c in sorted_by_name[:5]])
# print("Countries sorted by capital:", [c["name"] for c in sorted_by_capital[:5]])
# print("Countries sorted by population:", [c["name"] for c in sorted_by_population[:5]])
