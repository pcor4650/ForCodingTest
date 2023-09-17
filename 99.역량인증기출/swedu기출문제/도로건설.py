# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# user_input = input()
# print ("Hello Goorm! Your input is " + user_input)

# 아래 위 코드 비교해보기

# import sys
# from heapq import *			#deque로 바꾸니 일부 TC 오답처리됨
# read=sys.stdin.readline

# INF = 987654321
# dir = [[0,1],[0,-1],[1,0],[-1,0]]
# N = int(read())
# board = []
# for _ in range(N):
# 	board.append(list(map(int, list(read().strip()))))		#입력으로 배열 생성

# dist = [[INF for _ in range(N)] for _ in range(N)]
# dist[0][0] = 0
# Q = [[0,0,0]]
# while Q:
# 	w,y,x = heappop(Q)
# 	if y==N-1 and x==N-1 : break	#(N-1,N-1) 좌표에 도착 시 종료
# 	if w>dist[y][x]:continue	#
	
# 	for dy,dx in dir:
# 		ny, nx = y+dy, x+dx
# 		if 0 <= ny <N and 0 <= nx < N :			#이동한 좌표가 정상 범위에 있으면서, w: 기존 거리 합, 
# 			dist[ny][nx] = w + board[ny][nx]
# 			Q.append([dist[ny][nx],ny,nx])

# print(dist[N-1][N-1])

#deque으로 풀어보자

# import sys
# from heapq import *
# read = sys.stdin.readline

# INF = 987654321
# dir = [[0,1],[0,-1],[1,0],[-1,0]]
# N = int(read())
# board = []
# for _ in range(N):
#     board.append(list(map(int,list(read().strip()))))

# dist = [[INF for _ in range(N)] for _ in range(N)]
# dist[0][0]=0
# Q = [[0,0,0]]
# while Q:
#     w,y,x = heappop(Q)
#     if y==N-1 and x==N-1:break
#     if w>dist[y][x]:continue
#     for dy,dx in dir:
#         ny,nx = y+dy, x+dx
#         if 0<=ny<N and 0<=nx<N and dist[ny][nx]>w+board[ny][nx]:
#             dist[ny][nx] = w+board[ny][nx]
#             Q.append([dist[ny][nx],ny,nx])
# print(dist[N-1][N-1])

# import sys
# from collections import deque

# def input_data():
# 	readl = sys.stdin.readline
# 	N = int(readl())
# 	map_cost = [
# 		list(map(int, readl()[:-1]))
# 		for r in range(N)
# 	]
# 	return N, map_cost

# sol = -2

# # 입력받는 부분
# N, map_cost = input_data()

# # 여기서부터 작성
# dir = [[1,0], [-1,0], [0,1], [0,-1]]
# INF = 999999999
# dist = [[INF]*N for _ in range(N)]

# def bfs(sy, sx):
#     q = deque()
#     q.append([sy,sx])
#     dist[sy][sx] = 0
#     while q:
#         y, x = q.popleft()
#         for dy, dx in dir:
#             ny, nx = y+dy, x+dx
#             if 0<= ny < N and 0<= nx < N and dist[ny][nx] > dist[y][x] + map_cost[ny][nx]:
#                 dist[ny][nx] = dist[y][x] + map_cost[ny][nx]
#                 q.append([ny, nx])
                
# bfs(0,0)
# print(dist[N-1][N-1])



# 입력:
# 3
# 041
# 253
# 620

# 출력:
# 8


import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
eachCostMap = [list(map(int, input().strip())) for _ in range(N)]

dir = [[0,1], [0,-1],[1,0],[-1,0]]
INF = 9876543210
totalCostMap = [[INF]*N for _ in range(N)]

def bfs(sy, sx):
    q = deque()
    q.append([sy, sx])
    totalCostMap[sy][sx] = 0
    while q:
        y, x = q.popleft()
        for dy, dx in dir:
            ny, nx = y+dy, x+dx
            if 0<=ny<N and 0<=nx<N and totalCostMap[ny][nx] > totalCostMap[y][x] + eachCostMap[ny][nx]:
                totalCostMap[ny][nx] = totalCostMap[y][x] + eachCostMap[ny][nx]
                q.append([ny, nx])

bfs(0, 0)
print(totalCostMap[N-1][N-1])