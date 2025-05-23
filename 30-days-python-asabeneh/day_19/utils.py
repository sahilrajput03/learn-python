import urllib.request
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


def readEmailsBigFromTxtFile():
    dirname = os.path.dirname(os.path.dirname(__file__))
    data_file = os.path.join(dirname, "data", "email_exchanges_big.txt")

    with open(data_file, "r") as f:
        emails_data = f.read()
    return emails_data


# Fetching text file content from a url using *native* `urllib` module of python
def readTextFileFromUrlViaNativeModule(fileUrl):
    try:
        response = urllib.request.urlopen(fileUrl)
        data = response.read().decode()  # Default argument value of `decode` is 'utf-8'
        return data
    except urllib.error.URLError as e:
        print(f"Error accessing URL: {e}")
        return 0


# ChatGPT - https://chatgpt.com/c/67ebbfb9-8280-8007-b4e8-b709ee406881
# Key Differences from requests (From ChatGPT)
"""
Feature             urllib.request	            requests
==========================================================================
Ease of Use         Less user-friendly	        More intuitive
Built-in?           Yes (comes with Python)	    Needs pip install requests
Exception Handling	Requires manual handling	Built-in error handling
Performance	        Similar	                    Similar
"""
