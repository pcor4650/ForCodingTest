# https://swedu.lge.com/learn/lecture/321/mooc-sw%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-%EC%97%AD%EB%9F%89%EC%9D%B8%EC%A6%9D%EC%8B%9C%ED%97%98-%EA%B8%B0%EC%B6%9C%EB%AC%B8%EC%A0%9C-%ED%95%B4%EC%84%A4/lesson/8815/%EA%B7%B8%EB%A6%BC%EC%9D%B8%EC%8B%9D

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys

def input_data():
	readl = sys.stdin.readline
	N = int(readl())
	map_pic = [list(map(int, readl().strip())) for _ in range(N)]
	return N, map_pic


sol = -1
# 입력받는 부분
N, map_pic = input_data()
color = set()
check = [0]*(10)

# 여기서부터 작성
for i in range(N):
    for j in range(N):
        if map_pic[i][j] != 0:
            color.add(map_pic[i][j])

pos = dict()
for c in color:
    check[c] = 1
    y1, x1, y2, x2 = 11, 11, -1, -1
    for i in range(N):
        for j in range(N):
            if map_pic[i][j] == c:
                y1, x1, y2, x2 = min(y1, i), min(x1, j), max(y2, i), max(x2, j) 
    pos[c] = [y1, x1, y2, x2]


for k, v in pos.items():
    # print(k, v)
    for i in range(v[0], v[2]+1):
        for j in range(v[1], v[3]+1):
            if map_pic[i][j] != k:
                check[map_pic[i][j]] = 0

print(sum(check))