# SUBMITTED THIS SOLUTION:
# This code passed all 5 test cases.
# src: https://github.com/hirenvasani/foobar/blob/master/prepare_the_bunnies_escape.py
def sht_pth(x, y, map):
    c = len(map[0])
    r = len(map)
    board = [[None for i in range(c)] for i in range(r)]
    board[x][y] = 1

    arr = [(x, y)]
    while arr:
        u, v = arr.pop(0)
        for i in [[1,0],[-1,0],[0,-1],[0,1]]:
          a, b = u + i[0], v + i[1]
          if 0 <= a < r and 0 <= b < c:
            if board[a][b] is None:
                board[a][b] = board[u][v] + 1
                if map[a][b] == 1 :
                  continue
                arr.append((a, b)) 
                  
    return board

def solution(map):
  r = len(map)
  c = len(map[0])
  tb = sht_pth(0, 0, map)
  bt = sht_pth(r-1, c-1, map)
  board = []

  result = 2 ** 32-1
  for i in range(r):
      for j in range(c):
          if tb[i][j] and bt[i][j]:
              result = min(tb[i][j] + bt[i][j] - 1, result)
  return result

print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))