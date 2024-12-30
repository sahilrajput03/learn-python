# bakchodi
text = "HelLOO"

# print all available methods on this value
print(dir(text))

print(text.upper())  # HELLOO
print(text.lower())  # helloo

print(text.startswith("Hel"))  # True
print(text.startswith("ABC"))  # False

person_info = {
    "firstname": "Asabeneh",
    "lastname": "Yetayeh",
    "country": "Finland",
    "city": "Helsinki",
}

print(person_info)
