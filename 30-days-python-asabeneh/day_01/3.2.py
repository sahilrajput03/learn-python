# Nested list comprehension example.
myLambda = lambda a, b, sum: a + b != sum  # Returns True or False

X = range(3)  # [0, 1, 2 , ...n-1]
Y = range(2)

# PRINTS ALL THE POINTS IN TWO-DIMENSION SPACE.
points = [[xval, yval] for xval in X for yval in Y]  # Prints all the points.
print(points)  # [[0, 0], [0, 1], [1, 0], [1, 1], [2, 0], [2, 1]]

# Note to Sahil: This above syntax of nested loop works like
# `for Loop1 for Loop2`
# Loop1 (e.g., X values in this case)
#       Loop2 (e.g, Y values in this case)


# Print values only when sum of values is `required_sum`
required_sum = 3

points = [
    [xval, yval] for xval in X for yval in Y if xval + yval != required_sum
]  # SIMPLE SOLUTION.
print(points)  # [[0, 0], [0, 1], [1, 0], [1, 1], [2, 0]]
# We learn in this example that we can pass a condition after the `for-loop` and return values if that condition passes.


points = [
    [xval, yval] for xval in X for yval in Y if myLambda(xval, yval, required_sum)
]  # SOLUTION USING LAMBDA FUNCTION.
print(points)  # [[0, 0], [0, 1], [1, 0], [1, 1], [2, 0]]
# We learn in this example that we can pass a lambda function after the `for-loop` and condition returned from
#   lambda function will judge whether to show a variable


# Sahil: Probably these ways are helpful in using when we need functionalities
# similar to `find` or `filter` array methods in Javascript.
