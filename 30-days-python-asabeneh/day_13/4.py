# Lambda Function Inside Another Function
def power(x):
    return lambda n: x**n


# Learn: Here `2` is `x` and `3` is `n` thus --- 2**3 = 8
print(power(2)(3))  # 8

# Learn: Here `2` is `x` and `5` is `n` thus --- 2**5 = 32
print(power(2)(5))  # 32
