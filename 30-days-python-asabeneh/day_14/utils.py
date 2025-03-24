import json
import os


# * Prompt to Copilot for reading json file:
#       Read file `countries_data.json` from `data` folder which is present in
#               parent folder of current script.
def readCountriesFromJsonFile():
    dirname = os.path.dirname(os.path.dirname(__file__))
    data_file = os.path.join(dirname, "data", "countries_data.json")

    with open(data_file, "r") as f:
        countries_data = json.load(f)
    return countries_data
