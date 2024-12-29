# Nested list comprehension example.
myLambda = lambda a, b, c, sum: a + b + c != sum  # Returns True or False

X = range(2)  # [0, 1, 2 , ...n-1]
Y = range(2)
Z = range(2)

# PRINTS ALL THE POINTS IN SPACE.
points = [
    [xval, yval, zval] for xval in X for yval in Y for zval in Z
]  # Prints all the points.
print(
    points
)  # [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]


# Print values only when sum of values is `required_sum`
required_sum = 2

points = [
    [xval, yval, zval]
    for xval in X
    for yval in Y
    for zval in Z
    if xval + yval + zval != required_sum
]  # SIMPLE SOLUTION.
print(points)  # [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
# We learn in this example that we can pass a condition after the `for-loop` and return values if that condition passes.

points = [
    [xval, yval, zval]
    for xval in X
    for yval in Y
    for zval in Z
    if myLambda(xval, yval, zval, required_sum)
]  # SOLUTION USING LAMBDA FUNCTION.
print(points)  # [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
# We learn in this example that we can pass a lambda function after the `for-loop` and condition returned from
#   lambda function will judge whether to show a variable


# Sahil: Probably these ways are helpful in using when we need functionalities
# similar to `find` or `filter` array methods in Javascript.
