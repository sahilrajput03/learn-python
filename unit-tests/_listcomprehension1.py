# src: https://www.w3schools.com/python/python_lists_comprehension.asp
# 🤺︎ It can be used like we use `map` of array methods in javascript or like `filter` of array methods in javascript depending upon if you specify the condition in the end of the list comprehension.
x = int(input("Enter x\n"))
X = range(x)  # X [0, 1, 2 , ...x-1]

m1 = [i for i in X]
#     ^ here this is the return value and it works exactly like map function in javascript.
print(m1)
