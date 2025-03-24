# Ex7: Write a lambda function which can solve a slope or y-intercept of linear functions.
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
y_intercept = lambda x, y, m: y - (m * x)  # `y=mx+c`

# Example usage
x1, y1 = 0, 1  # First point
x2, y2 = 2, 5  # Second point

m = slope(x1, y1, x2, y2)
b = y_intercept(x1, y1, m)  # when x=0

print(f"Slope (m): {m}")
print(f"Y-intercept (b): {b}")
