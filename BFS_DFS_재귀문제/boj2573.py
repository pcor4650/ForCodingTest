import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dir = [[1,0],[-1,0],[0,1],[0,-1]]

# (sy, sx)에 연결된 노드에 대해 업데이트 수행
def bfs(sy, sx):
    q = deque()
    q.append((sy, sx))
    visited[sy][sx] = 1
    seaList = [] #sy, sx 좌표의 인접한 바다가 몇개인지 저장하기 위한 리스트

    while q:
        y, x = q.popleft()
        sea = 0
        for dy, dx in dir:
            ny, nx = y+dy, x+dx
            if 0<=ny<N and 0<=nx<M:
                if board[ny][nx] == 0:
                    sea += 1
                elif board[ny][nx] and visited[ny][nx] == 0:
                    q.append((ny, nx))  # y, x에 인접하는 노드를 모두 q에 넣어줌
                    visited[ny][nx] = 1
        if sea > 0:
            seaList.append((y, x, sea))
    # q에 있는 모든 노드 순회 후 일괄적으로 값 업데이트
    for y, x, sea in seaList:
        board[y][x] = max(0, board[y][x]-sea)
    
    return 1

# 얼음 영역 모두 q에 삽입
ice = []
for i in range(N):
    for j in range(M):
        if board[i][j] != 0:
            ice.append((i, j))

year = 0
while ice:
    visited = [[0]*M for _ in range(N)]
    delList = []
    group = 0
    for i, j in ice:
        if board[i][j] != 0 and visited[i][j] == 0:
            group += bfs(i, j)
        if board[i][j] == 0:
            delList.append((i, j))  # 아이스였던 영역이 바다가 되면 delList에 추가
    if group > 1:
        print(year)
        break
    ice = list(set(ice) - set(delList))
    year += 1    

if group < 2:
    print(0)