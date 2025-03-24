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
positive_even_numbers = [
    i  # Here i is from last line
    for i in numbers
    if i % 2 == 0 and i > 0  # Here `i` is from above line
]
print(positive_even_numbers)  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Flattening a three dimensional list/array
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [
    item  # Here `item` variable is from last line
    for list in list_of_lists
    for item in list  # Here `list` variable is from above line
]
print(flattened_list)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
