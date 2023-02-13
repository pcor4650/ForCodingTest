import sys
sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
INF = 987654321


dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def dfs(sy, sx):
    board[sy][sx] = 2
    for dy, dx in dir:
        ny, nx = sy+dy, sx+dx
        if 0 <= ny < N and 0 <= nx < M and board[ny][nx] == 1:
            dfs(ny, nx)

flag = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            dfs(i, j)
            flag = 1
            break
    if flag:
        break

def bfs(sy, sx):
    dist = [[INF]*M for _ in range(N)]
    dist[sy][sx] = 0
    Q = deque()
    Q.append([sy, sx])
    while Q:
        y, x = Q.popleft()
        if board[y][x] == 1:
            return dist[y][x] -1
        for dy, dx in dir:
            ny, nx = y+dy, x+dx
            if 0 <= ny < N and 0 <= nx < M and board[ny][nx] != 2 and dist[ny][nx]>dist[y][x]+1:
                dist[ny][nx] = dist[y][x]+1
                Q.append([ny, nx])
    return INF

sol = INF
for i in range(N):
    for j in range(M):
        if board[i][j] == 2:
            sol = min(sol, bfs(i, j))
print(sol)    