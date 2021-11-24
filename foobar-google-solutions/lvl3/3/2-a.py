import pprint
Hmax,Wmax,map = 0,0,[]

def isValid(x,y):
    global Hmax,Wmax
    # print('values of hmax and wmax', Hmax, Wmax)
    # print('isValid', x, y)
    if x >= 0 and x < Wmax and y >= 0 and y < Hmax:
        return True
    else:
        return False

class Node:
    def __init__(self, x, y):
        print('node created:', x, y)
        self.x = x
        self.y = y
        global map
        self.data = map[y][x]

        self.right = None
        self.down = None
        self.left = None
        self.up = None
 
def bfs(root, level):
    if root is None:
        return
    if level == 1:
        if isValid(root.x+1, root.y) and map[root.y][root.x+1] == 0:
            root.right = Node(root.x+1, root.y)
        if isValid(root.x, root.y+1) and map[root.y+1][root.x] == 0:
            root.down = Node(root.x, root.y+1)
        if isValid(root.x-1, root.y) and map[root.y][root.x-1] == 0:
            root.left = Node(root.x-1, root.y)
        if isValid(root.x, root.y-1) and map[root.y-1][root.x] == 0:
            root.up = Node(root.x, root.y-1)

    elif level > 1:
        if isValid(root.x+1, root.y) and map[root.y][root.x+1] == 0:
            bfs(root.right, level-1)

        if isValid(root.x, root.y+1) and map[root.y+1][root.x] == 0:
            bfs(root.down, level-1)

        if isValid(root.x-1, root.y) and map[root.y][root.x-1] == 0:
            bfs(root.left, level-1)
 
        if isValid(root.x, root.y-1) and map[root.y-1][root.x] == 0:
            bfs(root.up, level-1)

def solution(M):
        print('Called solution function...')
        p, q, isEscaped, failedEscapes, steps, H, W = 0, 0, False, [], 1, len(M), len(M[0]) # length of first of list in map.

        global map,Hmax, Wmax
        Hmax,Wmax,map = H-1, W-1, M
        print("Level order traversal of binary tree is -")

        #! give here the root tree.
        root = Node(0,0)
        height = 51
        for i in range(1, height):
            print('FOR HEIGHT ', i)
            bfs(root, i)
 
# This code is contributed by Nikhil Kumar Singh(nickzuck_007)
print('Got solution as:', solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))

# Driver program to test above function
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)