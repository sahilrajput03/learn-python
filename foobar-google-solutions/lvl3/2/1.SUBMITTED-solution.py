import time
# src: https://stackoverflow.com/a/61563604
def solution(l):
    c = [0] * len(l)
    print('list ',l)
    print('org-c', c)
    print('')
    count = 0
    for i in range(0,len(l)):
        for j in range(0, i):
            if l[i] % l[j] == 0:
            # Here,   ^^ l[j] is any left-child (l[j]) in the list to the element we're iterating on (l[i]). ~sahil.
                c[i] = c[i] + 1 # We increment current by one coz the current is divisible by l[j] ~sahil.
                count = count + c[j]
                # Here,         ^^ we increment count by the no. factors that the left-child has ~sahil.
                print(l[i],',',l[j])
                print(f'i:{i}, j:{j}')
                print('new-c',c,)
                if c[j] != 0:
                    print(f'->                               j={j}, l[{j}]={l[j]},  c[{j}]={c[j]} factors,  count={count}')
                print()
    return count

start = time.perf_counter()

# print(solution([1,1,1]))
# print(solution([1,2,3]))
# print(solution([1,2,3,4,5,6]))
print(solution([1,2,3,4,5,6,7,8]))
# print(solution([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]))
end = time.perf_counter()
# print('time took',end  - start)