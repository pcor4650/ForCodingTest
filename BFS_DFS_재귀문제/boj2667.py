import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
board = [list(map(int, input().strip())) for _ in range(N)]

INF = 9876543210
visited = [[0]*N for _ in range(N)]
dir = [[1,0], [-1,0],[0,1],[0,-1]]

def bfs(sy, sx, idx):
    visited[sy][sx] = 1
    apt_num[idx] = 1
    board[sy][sx] = idx
    q = deque()
    q.append([sy, sx])
    while q:
        y, x = q.popleft()
        for dy, dx in dir:
            ny, nx = y+dy, x+dx
            if 0<=ny<N and 0<=nx<N and board[ny][nx] == 1 and visited[ny][nx]==0:
                visited[ny][nx] = 1
                apt_num[idx] += 1
                board[ny][nx] = idx
                q.append([ny, nx])
                
apt_num = {}
idx = 0
for i in range(N):
    for j in range(N):
        if board[i][j] != 0 and visited[i][j]==0:
            idx += 1
            bfs(i, j, idx)


print(len(apt_num))
aptNum = sorted(apt_num.values())
for k in aptNum:
    print(k)

# print(apt_num)

# for k in board:
#     print(k)