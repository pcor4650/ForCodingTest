import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(N)]
INF = 9876543210
dist = [[INF]*M for _ in range(N)]
dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]

# for k in board:
#     print(k)

def bfs(sy, sx):
    dist[sy][sx] = 1
    Q = deque()
    Q.append([sy, sx])
    while Q:
        y, x = Q.popleft()
        for dy, dx in dir:
            ny, nx = y+dy, x+dx
            if 0<=ny<N and 0<=nx<M:
                if board[ny][nx] != 0 and dist[ny][nx] > dist[y][x] + 1:
                    dist[ny][nx] = dist[y][x] + 1
                    Q.append([ny, nx])
    return dist[N-1][M-1]


sol = bfs(0, 0)

# bfs(0, 0)
# for k in dist:
#     print(k)

print(sol)

