map = []
def move(x,y):
    global map
    # print('\nfrom:', x,y)
    if x < len(map[0]) - 1 and map[y][x+1] == 0 : return [x+1,y]
    # print('incrementing y',map[y+1][x])
    if y < len(map) - 1 and map[y+1][x] == 0: return [x, y+1]
    return None
    # if x < len(map[0]) - 1 and map[y][x-1] == 0: return [x-1, y]
    # if y < len(map) - 1 and map[y-1][x] == 0: return [x, y-1]

def solution(M):
    print('Called solution function...')
    p, q, isEscaped, failedEscapes, steps, H, W = 0, 0, False, [], 1, len(M), len(M[0]) # length of first of list in map.

    global map
    map = M
    shouldMove = True
    while shouldMove == True:
        steps += 1
        F = move(p,q)
        if F == None:
            if isEscaped == False:
                print('escaping this time...')
                isEscaped = True
                if [p,q+1] in failedEscapes:
                    p = p+1
                else:
                    q = q+1
                print('to', [p,q])
            else:
                print('resetting game:')
                isEscaped = False
                failedEscapes.append([p,q])
                p, q = 0, 0
        else:
            p, q = F[0], F[1]
            print('to', F)
            if( [p, q] == [H-1, W-1]):
                shouldMove = False

    return steps


    # Y = len(map)
    # X = len(map[0]) # length of first of list in map.

    # for y in range(Y):
    #     for x in range(X):
    #  3      print(map[y][x])
    #     print()
# print('Got solution as:', solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]))
print('Got solution as:', solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))

