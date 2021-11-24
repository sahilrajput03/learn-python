import math
class cell:
     
    def __init__(self, x = 0, y = 0, dist = 0):
        self.x = x
        self.y = y
        self.dist = dist
         
def checkIfInside(x, y, N):
    if (x >= 1 and x <= N and
        y >= 1 and y <= N):
        return True
    return False
     
def calculateMinimumSteps(inputSrc, inputDest):
    N = 64
    dx = [2, 2, -2, -2, 1, 1, -1, -1]
    dy = [1, -1, 1, -1, 2, -2, 2, -2]
     
    myQueue = []
     
    myQueue.append(cell(inputSrc[0], inputSrc[1], 0))
    k = []
     
    vstd = [[False for i in range(N + 1)]
                      for j in range(N + 1)]
    j = []
     
    vstd[inputSrc[0]][inputSrc[1]] = True
     
    kxx = []
    while(len(myQueue) > 0):
         
        t = myQueue[0]
        myQueue.pop(0)
         
        if(t.x == inputDest[0] and
           t.y == inputDest[1]):
            return t.dist
             
        for i in range(8):
             
            x = t.x + dx[i]
            y = t.y + dy[i]
             
            if(checkIfInside(x, y, N) and not vstd[x][y]):
                vstd[x][y] = True
                myQueue.append(cell(x, y, t.dist + 1))
 
def solution(src, dest):
    x = [src % 8 + 1, math.floor(src / 8) + 1] # src + 1
    y = [dest % 8 + 1, math.floor(dest / 8) + 1]

    return calculateMinimumSteps(x, y)
    

print(solution(0, 1)) # sol: 3
# print(solution(19, 36)) # sol: 1
# print(solution(19, 19)) # sol: 0
# print(solution(34, 38)) # sol: 2