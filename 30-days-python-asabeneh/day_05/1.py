# source -
# https://github.com/Asabeneh/30-Days-Of-Python/blob/master/05_Day_Lists/day_5.py

empty_list = list()  # this is an empty list, no item in the list
print(len(empty_list))  # 0
print(len(empty_list) == 0)  # True

fruits = ["banana", "orange", "mango", "lemon"]  # list of fruits
print(fruits)  #  ['banana', 'orange', 'mango', 'lemon']
print(len(fruits))  # 4
print(fruits[0])  # banana
print(fruits[1])  # orange
print(fruits[len(fruits) - 1])  # lemon
print(fruits[-2])  # mango (accessing second last item)

# Slicing items
fruits = ["banana", "orange", "mango", "lemon"]
print(fruits[0:4])  # returns all the fruits

#  If we don't set where to stop it takes all the rest
print(fruits[0:])  # returns all the fruits as above

# exclude first item and the last item (Note: item at index 3 is excluded)
print(fruits[1:3])  # ['orange', 'mango']
print(fruits[1:])  # ['orange', 'mango', 'lemon']
