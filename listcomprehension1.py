# src: https://www.w3schools.com/python/python_lists_comprehension.asp
x = int(input('Enter x\n'))

X = range(x) # X [0, 1, 2 , ...x-1]

m1 = [ i for i in X]

print(m1)