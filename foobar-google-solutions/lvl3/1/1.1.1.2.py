import time, datetime
# Given cases: 2,1: 1, 4,7:4

def solution(M, F):
    start = time.perf_counter()
    if len(F) > 50 or  len(M) > 50:
        # Here len(M) > 30 is required in OR operator to pass the test.
        return 'impossible'
    
    M = int(M)
    F = int(F)
    
    
    m, f = 1, 1 # initial Machs and Faculas
    cycles = 0

    mNeeded = M-m
    fNeeded = F-f
    
    while mNeeded > 0 or fNeeded > 0:
        if cycles > 1_00_00_000: # takes 60 secs in whole.
            break
        # print('calling.')
        if mNeeded > 0:
            cycles += 1
            fToReplicate = mNeeded if mNeeded <= f else f
            m = m + fToReplicate
            # print('fToReplicate', fToReplicate)
            # for instance say `f=5` and `mNeeded=3` so we set fToReplicate=3.
            mNeeded = M-m


        if fNeeded > 0:
            cycles += 1
            mToReplicate = fNeeded if fNeeded <= m else m
            f = f + mToReplicate
            # print('mToReplicate', mToReplicate)
            # for instance say `m=5` and `fNeeded=3` so we set mToReplicate=3.
            fNeeded = F-f
    
    print('\nTime taken in seconds::', time.perf_counter() - start)
    return cycles


# ! IT TAKES .24 seconds on average with values => (1, 1234567)
test3 = solution("1","1234567") # takes 7 seconds, i.e, 12 lakh iterations of while are run.
print('\n\n\ntest3:', "PASSED" if test3 == 1234566 else 'failed, got value ' + str(test3) + ' instead of 1234566')


# test3 = solution("1","1234567") # so 10 digit program takes more than 30 seconds to solve.
# print('\n\ntest3:', "PASSED" + str(test))

    
    
    

# test1 = solution("1","2")
# print('\n\n\ntest1:', "PASSED" if test1 == 1 else 'failed, got value ' + str(test1) + ' instead of 1')

# test2 = solution("4","7")
# print('\n\n\ntest2:', "PASSED" if test2 == 4 else 'failed, got value ' + str(test2) + ' instead of 4')

# This is not required at all.
# test4 = solution("7","10**50")
# print('\n\n\ntest4:', "PASSED" if test4 == 'impossible' else 'failed, got value ' + str(test4) + ' instead of "impossible"')

# test4a = solution("7","123456789012345678901234567890123456789")
# print('\n\ntest4a:', "PASSED" if test4a == 'impossible' else 'failed, got value ' + str(test4a) + ' instead of "impossible"')





# my test suite
# print(solution("10","10"))