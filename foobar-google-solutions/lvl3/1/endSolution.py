def solution(x, y):
    if "**" in y or "**" in x:
    # if a >= 10**50 or b >= 10**50:
        return "impossible"

    a = int(x)
    b = int(y)
    # if b >= 10**50 or a >= 10**50:
        # return "impossible"
    # elif b > a:
    if b > a:
        return str(a)
    elif a > b:
        return str(b)
    elif a == b:
        return "0"