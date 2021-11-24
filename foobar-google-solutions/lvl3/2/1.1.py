import time
# [1,2,3,4,5,6]: 3
# [1,1,1]: 1

def rescur(l):
    m = max(l)  
    l.remove(m); 
    factor = [x for x in l if m%x==0]
    return factor

def fl(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact

def twoC(num):
    one = fl(num)/2
    two = fl(num-2)
    return one / two


def solution(l):
    setL = set(l)
    if len(setL) == 1:
        return 1
    
    no_of_triples = 0
    for x in l:
        fact = rescur(l)
        if len(fact) > 1:
            no_of_triples += twoC(len(fact))
    return int(no_of_triples-1)

l = [1,2,3,4,5,6, 7, 8]
l = [1,1,1]
print(solution(l))

start = time.perf_counter()
# print(solution([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,52,33,34,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,52,33,34,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,52,33,34,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,52,33,34,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,52,33,34,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,52,33,34]))
end = time.perf_counter()

# print('time took:', end - start)