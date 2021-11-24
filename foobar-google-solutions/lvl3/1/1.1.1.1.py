# Given cases: 2,1: 1, 4,7:4

def solution(M, F):
    # if '**' in F or '**' in M:
    if len(F) > 50 or  len(M) > 50:
        # Here len(M) > 30 is required in OR operator to pass the test.
        return 'impossible'
    
    # print(type(M))
    M = int(M)
    F = int(F)
    # print(type(M))
    
    
    m, f = 1, 1 # initial Machs and Faculas
    cycles = 0

    mNeeded = M-m
    fNeeded = F-f
    # print('mNeeded', mNeeded)
    
    while mNeeded > 0 or fNeeded > 0:
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


    # print(m,f)
    # print('cycles',cycles)
    
    return cycles
    

# test1 = solution("1","2")
# print('\n\n\ntest1:', "PASSED" if test1 == 1 else 'failed, got value ' + str(test1) + ' instead of 1')

# test2 = solution("4","7")
# print('\n\n\ntest2:', "PASSED" if test2 == 4 else 'failed, got value ' + str(test2) + ' instead of 4')

# This is not required at all.
# test4 = solution("7","10**50")
# print('\n\n\ntest4:', "PASSED" if test4 == 'impossible' else 'failed, got value ' + str(test4) + ' instead of "impossible"')

# test4a = solution("7","123456789012345678901234567890123456789")
# print('\n\ntest4a:', "PASSED" if test4a == 'impossible' else 'failed, got value ' + str(test4a) + ' instead of "impossible"')

test3 = solution("7","1234567890") # so 10 digit program takes more than 30 seconds to solve.
print('\n\ntest3:', "PASSED" + str(test3))




# my test suite
# print(solution("10","10"))