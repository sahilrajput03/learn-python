# ex4: Get the first item, the middle item and the last item of the list
lst = ["Asabeneh", 250, True, {"country": "Finland", "city": "Helsinki"}, False]
print(lst[0])  # first item
print(lst[int((len(lst) + 1) / 2)])  # middle item
print(lst[len(lst) - 1])  # last item

print("\n", lst)


# ex10: Print the list after modifying one of the companies
lst = ["item1", "item2", "item3", "item4", "item5"]
lst[0] = "item101"
print("\n", lst)

# ex12: Insert an IT company in the middle of the companies list
it_companies = ["twitter", "facebook"]
it_companies.insert(int(len(it_companies) / 2), "😍google")
print(it_companies)

# ex.13: Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[1] = it_companies[1].upper()
print(it_companies)

# ex.14: Join the it_companies with a string '#;  '
countries_string = "#; ".join(it_companies)
print(countries_string)


# ex.15: Check if a certain company exists in the it_companies list (incase-sensitive checking)
companyToCheck = "FaceBook"
if companyToCheck.lower() in [company.lower() for company in it_companies]:
    print(f"{companyToCheck} exists in the list")
else:
    print(f"{companyToCheck} does not exist in the list")

# TODO: ex.19: Slice out the last 3 companies from the list
# https://github.com/Asabeneh/30-Days-Of-Python/blob/master/05_Day_Lists/05_lists.md
