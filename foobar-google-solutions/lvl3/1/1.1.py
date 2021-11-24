# Given cases: 2,1: 1, 4,7:4

def solution(M, F):
    # print(type(M))
    M = int(M)
    F = int(F)
    # print(type(M))
    
    
    m, f = 1, 1 # initial Machs and Faculas
    cycles = 0

    mNeeded = M-1
    fNeeded = F-1
    # print('mNeeded', mNeeded)
    
    if mNeeded > 0:
        cycles += 1
        fToReplicate = mNeeded if mNeeded <= f else f
        m = m + fToReplicate
        # print('fToReplicate', fToReplicate)
        # for instance say `f=5` and `mNeeded=3` so we set fToReplicate=3.

    if fNeeded > 0:
        cycles += 1
        mToReplicate = fNeeded if fNeeded <= m else m
        f = f + mToReplicate
        # print('mToReplicate', mToReplicate)
        # for instance say `m=5` and `fNeeded=3` so we set mToReplicate=3.

    print(m,f)
    # print('cycles',cycles)
    
    return cycles
    

test1 = solution("1","2")
print('\n\n\ntest1:', "PASSED" if test1 == 1 else 'failed, got value ' + str(test1) + ' instead of 1')

# test2 = solution("4","7")
# print('\n\n\ntest2:', "PASSED" if test2 == 4 else 'failed, got value ' + str(test2) + ' instead of 4')






# print(solution("4","7"))
# print(solution("7","10**50")) # mimicing test case 3 which required "impossible" string.

# my test suite
# print(solution("10","10"))



