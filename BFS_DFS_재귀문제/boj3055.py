# 내 코드로 고쳐보자

import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().split())
board = []
for _ in range(R):
  board.append(list(map(str, input().strip())))

visit = [[0]*C for _ in range(R)]

Q = deque()
for row in range(R):
  for col in range(C):
    if board[row][col] == '*':
      Q.append([row, col])
    elif board[row][col] == 'S':
      hodgedog = [row, col]
    elif board[row][col] == 'D':
      goal_r, goal_c  = row, col

Q.appendleft(hodgedog)



dir = [[1,0],[-1,0],[0,1],[0,-1]]

def bfs(board, Q):
  flag = False
  while Q:
    y, x = Q.popleft()
    if flag:
      break
    for dy, dx in dir:
      ny, nx = y+dy, x+dx
      if 0<=nx<C and 0<=ny<R:
        if board[y][x] == '*':
          if board[ny][nx] == '.' or board[ny][nx] == 'S':
            board[ny][nx] = '*'
            Q.append([ny, nx])
        elif board[y][x] == 'S': 
          if board[ny][nx] == '.':
            board[ny][nx] = 'S'
            visit[ny][nx] = visit[y][x] + 1
            Q.append([ny,nx])
          elif board[ny][nx] == 'D':
            flag = True
            visit[ny][nx] = visit[y][x]+1
            break

bfs(board, Q)
if visit[goal_r][goal_c] == 0:
  print('KAKTUS')
else:
  print(visit[goal_r][goal_c])