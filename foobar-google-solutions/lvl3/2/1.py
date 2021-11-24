# [1,2,3,4,5,6]: 3
# [1,1,1]: 1

def solution(l):
    
    # case of [1,1,1] handled, [2,2,2]
    identical = l[0]
    setL = set(l)
    if l[0] == identical: return 1
    
    
    no_of_triples = 0
    # print(l)
    maximum = max(l)
    print('maximum:', maximum)

    factors = []
    for el in l:
        if maximum % el == 0 and el != maximum:
            factors.append(el)

    print('factors',factors)
    # for f in factors:
    
    return no_of_triples

print(solution([1, 2, 3, 4, 5, 6])) # desired output: 3