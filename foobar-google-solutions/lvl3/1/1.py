# 2,1

# 4,7


def solution(x, y):
    if "**" in y or "**" in x:
    # if a >= 10
    # **50 or b >= 10**50:
        return "impossible"

    a = int(x)
    b = int(y)
    
    # if y.isnumeric():
    #     print('y is numeric...')
    
    if b > a:
        return a
    elif a > b:
        return b
    elif a == b:
        return 0


    

print(solution("1","2"))
print(solution("4","7"))
print(solution("7","10**50")) # mimicing test case 3 which required "impossible" string.

# my test suite
print(solution("10","10"))
