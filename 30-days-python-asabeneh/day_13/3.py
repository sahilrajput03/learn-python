# Lambda function Synatx
# x = lambda param1, param2, param3: param1 + param2 + param2
# print(x(arg1, arg2, arg3))


# Named function
def sum1(a, b):
    return a + b


print(sum1(2, 3))  # 5

# Using lambda function
sum2 = lambda a, b: a + b
print(sum2(2, 3))  # 5

# Self invoking lambda function (Immediately Invoked Lambda Function)
print((lambda a, b: a + b)(100, 102))  # 202

square = lambda x: x**2
print(square(3))  # 9

cube = lambda x: x**3
print(cube(3))  # 27

# Multiple variables
y = lambda a, b, c: a**2 - 3 * b + 4 * c
print(y(5, 5, 3))  # 22
