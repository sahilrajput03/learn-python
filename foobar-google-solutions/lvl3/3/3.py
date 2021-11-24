# This code onlly passes 1st three test cases only.
# src: https://www.youtube.com/watch?v=Zscg5fICJLE&t=4s
def solution(map):
    def bfs(x,y,map):
        board = [[None for i in range(c)] for j in range(r)]
        board[x][y] = 1

        q = [(x,y)]
        while q:
            u,v = q.pop(0) # implementing first in first out, remove from left-most.
            for i,j in [(0,0),(0,-1),(1,0),(-1,0)]:
                a,b = u+i, v+j
                if 0 <= a < r and 0 <= b < c and board[a][b] is None:
                    board[a][b] = board[u][v] + 1
                    if map[a][b] != 1:
                        q.append([a,b])
        return board

    r = len(map)
    c = len(map[0])

    start_end = bfs(0,0,map)
    end_start = bfs(r-1,c-1,map)
    result = 999
    for i in range(r):
        for j in range(c):
            if start_end[i][j] and end_start[i][j]:
                result = min(result, start_end[i][j] + end_start[i][j] -1 )
    return result

print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))
