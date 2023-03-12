# 결과 : 시간 초과, 왜?
# 분석 : 1이 있는 모든 곳에서 bfs수행, 
# 변경방향 : 1이 있는 모든 곳에서 변경되도록 하려면?

import sys
input = sys.stdin.readline
from collections import deque

dir = [[1,0,0], [-1,0,0], [0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]
INF = 9876543210

M, N, H = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[0]*M for _ in range(N)] for _ in range(H)]
dist = [[[INF]*M for _ in range(N)] for _ in range(H)]

# (sh, sy, sx )좌표에 익은 사과가 있을 때 bfs를 통해 퍼지도록 작성
# def bfs (sh, sy, sx):
#     Q = deque()
#     Q.append([sh, sy, sx])
#     dist[sh][sy][sx] = 0
#     visited[sh][sy][sx] = 1
#     while Q:
#         h, y, x = Q.popleft()
#         for dh, dy, dx in dir:
#             nh, ny, nx = h+dh, y+dy, x+dx
#             if 0<=nh<H and 0<=ny<N and 0<=nx<M and box[nh][ny][nx] != -1:
#                 if box[nh][ny][nx] == 1 and visited[nh][ny][nx] == 0:
#                     continue
#                 if dist[nh][ny][nx] > dist[h][y][x] + 1:
#                     dist[nh][ny][nx] = dist[h][y][x] + 1
#                     box[nh][ny][nx] = 1
#                     visited[nh][ny][nx] = 1
#                     Q.append([nh, ny, nx])

# 박스 순회하며 익은데서만 bfs실행
# for k in range(H):
#     for i in range(N):
#         for j in range(M):
#             if box[k][i][j] == 1 and visited[k][i][j] ==0:
#                 bfs(k, i, j)

# 통과했지만 시간 단축 필요
# 익은 토마트 Q에 모두 넣기
Q = deque()
for k in range(H):
    for i in range(N):
        for j in range(M):
            if box[k][i][j] == 1:
                dist[k][i][j] = 0
                Q.append([k, i, j])
while Q:
    h, y, x = Q.popleft()

    for dh, dy, dx in dir:
        nh, ny, nx = h+dh, y+dy, x+dx
        if 0<=nh<H and 0<=ny<N and 0<=nx<M and box[nh][ny][nx] == 0:
            dist[nh][ny][nx] = dist[h][y][x] + 1
            box[nh][ny][nx] = 1
            visited[nh][ny][nx] = 1
            Q.append([nh, ny, nx])


# for k in box:
#     print(k)
# for k in dist:
#     print(k)

# 3차원 배열 -> 1차원 배열로 변경
flag = False
dayMax = 0
for k in range(H):
    for i in range(N):
        for j in range(M):
            if box[k][i][j] == 0:
                flag = True
            if dist[k][i][j] != INF:
                dayMax = max(dayMax, dist[k][i][j])

# print("boxFirst: ", boxFirst)
# print("distFirst: ", distFirst)


if flag == True:
    print(-1)
else:
    print(dayMax)