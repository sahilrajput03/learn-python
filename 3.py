# Nested list comprehentsion example.
# I stands for input from user.
x = int(input('Enter x\n'))
y = int(input('Enter y\n'))
z = int(input('Enter z\n'))
n = int(input('Enter n\n'))

myLambda = lambda a, b, c, d: a + b + c != d # this prints True or False.

X = range(x) # X [0, 1, 2 , ...x-1]
Y = range(y) # .. similarly for below
Z = range(z) #
N = range(n) #


# points = [[xval, yval, zval] for xval in X for yval in Y for zval in Z] # Prints all the points.

# SOLUTION BELOW:
points = [[xval, yval, zval] for xval in X for yval in Y for zval in Z if myLambda(xval, yval, zval, n)] # SOLUTION USING LAMBDA FUNCTION.
# points = [[xval, yval, zval] for xval in X for yval in Y for zval in Z if xval+yval+zval != n] # SIMPLE SOLUTION.


print(points)