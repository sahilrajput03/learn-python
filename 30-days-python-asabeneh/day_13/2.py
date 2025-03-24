# Generating even numbers
even_numbers = [
    i for i in range(21) if i % 2 == 0
]  # to generate even numbers list in range 0 to 21
print(even_numbers)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Generating odd numbers
odd_numbers = [
    i for i in range(21) if i % 2 != 0
]  # to generate odd numbers in range 0 to 21
print(odd_numbers)  # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Filter (getting) +ve even numbers from a `list` variable
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in numbers if i % 2 == 0 and i > 0]
print(positive_even_numbers)  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Flattening a three dimensional array
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [number for row in list_of_lists for number in row]
# There are 3 parts of above list comprehension:
# 1st: `for row in list_of_lists`
# 2nd: `for number in row` (Here `row` variable is from 1st part)
# 3rd: `number` (Here `number` variable is from 2nd part)
print(flattened_list)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
