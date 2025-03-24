# Ex1: Filter only negative and zero in the list using list comprehension
def negative_integers():
    list1 = [-4, -3, -2, -1, 0, 2, 4, 6]
    list2 = [i for i in list1 if i <= 0]
    list3 = [i for i in list1 if i == 0]
    return list2


negative_integers()
