import math
n = 8

x = n % 8 + 1
y = math.floor(n / 8) + 1


print('x,y:', str(x) + ',' + str(y))