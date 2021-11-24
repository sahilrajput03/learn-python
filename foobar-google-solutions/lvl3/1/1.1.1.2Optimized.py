import time, datetime
# Given cases: 2,1: 1, 4,7:4

def solution(x, y):
    M, F = max(int(x), int(y)), min(int(x), int(y))
    res = 0
    while F > 0:
        print('before')
        print('M,F, res', M, F, res)

        res += M // F
        M, F = F, M % F
        print('after')
        print('M,F, res', M, F, res)
        print('\n')

    if M != 1:
        return "impossible"
    return str(res - 1)


test8 = solution("2","4")
print('\n\n\ntest8:', "PASSED" if test8 == "impossible" else 'failed, got value ' + str(test8) + ' instead of 4')


# test7 = solution("4","7")
# print('\n\n\ntest7:', "PASSED" if test7 == "4" else 'failed, got value ' + str(test7) + ' instead of 4')

# takes .24 second on average
# test3 = solution("1","1234567") # takes 7 seconds, i.e, 12 lakh iterations of while are run.
# print('\n\n\ntest3:', "PASSED" if test3 == "1234566" else 'failed, got value ' + str(test3) + ' instead of 1234566')

# test5 = solution("1","12345678901234567890") # takes 7 seconds, i.e, 12 lakh iterations of while are run.
# print('\n\n\ntest5:', "PASSED" if test5 == "12345678901234567889" else 'failed, got value ' + str(test5) + ' instead of 1234566')


# test6 = solution("1","30") # takes 7 seconds, i.e, 12 lakh iterations of while are run.
# print('\n\n\ntest6:', "PASSED" if test6 == "29" else 'failed, got value ' + str(test6) + ' instead of 1234566')

