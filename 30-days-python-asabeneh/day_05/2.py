# Negative index examples
fruits = ["banana", "orange", "mango", "lemon"]
all_fruits = fruits[-4:]  # it returns all the fruits
# this is also give the same result as the above
orange_and_mango = fruits[-3:-1]  # it does not include the end index
print(orange_and_mango)  # ['orange', 'mango']

orange_mango_lemon = fruits[-3:]
print(orange_mango_lemon)  # ['orange', 'mango', 'lemon']
