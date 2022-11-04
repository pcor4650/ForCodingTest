# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# user_input = input()
# print ("Hello Goorm! Your input is " + user_input)

import sys

read = sys.stdin.readline

INF = 987654321
N, M = map(int, read().split())
A = [[INF for _ in range(N+1)] for _ in range(N+1)]	#왜?

for _ in range(M):
	u,v,c = map(int, read().split())
	A[u][v] = c
	A[v][u] = c     #u에서 v를 가능 거리와, v에서 u로 가는 거리는 같다

# k를 거쳐가는 방법
for k in range(1, N+1):
	for i in range(1, N+1):
		for j in range(1, N+1):
			if i==j : continue
			A[i][j] = min(A[i][j], A[i][k]+A[k][j])			##Fload Warshall 알고리즘

ans = []

for i in range(1, N+1):
	m = 0
	for j in range(1,N+1):
		if A[i][j] != INF:
			m = max(m, A[i][j])
	ans.append(m)

print(min(ans))

