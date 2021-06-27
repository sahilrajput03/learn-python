# src: https://www.w3schools.com/python/python_lists_comprehension.asp
x = int(input('Enter x\n'))

X = list(range(x))
print(X)
points = [item + 10 for item in X]
# first parameter is the return value i.e., `x + 2`
print(points)
