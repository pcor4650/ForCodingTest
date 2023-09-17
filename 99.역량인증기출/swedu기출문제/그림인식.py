# import sys

# def input_data():
# 	readl = sys.stdin.readline
# 	N = int(readl())
# 	map_pic = [list(map(int, readl().strip())) for _ in range(N)]
# 	return N, map_pic


# sol = -1
# # 입력받는 부분
# N, map_pic = input_data()
# color = set()
# check = [0]*(10)

# # 여기서부터 작성
# for i in range(N):
#     for j in range(N):
#         if map_pic[i][j] != 0:
#             color.add(map_pic[i][j])

# pos = dict()
# for c in color:
#     check[c] = 1
#     y1, x1, y2, x2 = 11, 11, -1, -1
#     for i in range(N):
#         for j in range(N):
#             if map_pic[i][j] == c:
#                 y1, x1, y2, x2 = min(y1, i), min(x1, j), max(y2, i), max(x2, j) 
#     pos[c] = [y1, x1, y2, x2]


# for k, v in pos.items():
#     # print(k, v)
#     for i in range(v[0], v[2]+1):
#         for j in range(v[1], v[3]+1):
#             if map_pic[i][j] != k:
#                 check[map_pic[i][j]] = 0

# print(sum(check))


import sys
input = sys.stdin.readline

N = int(input())
map_pic = [list(map(int, input().strip())) for _ in range(N)]

color = set()
check = [0]*10

for i in range(N):
    for j in range(N):
        if map_pic[i][j] != 0:
            color.add(map_pic[i][j])

color_pos = dict()
for c in color:
    check[c] = 1
    y1, x1, y2, x2 = 11, 11, -1, -1
    for i in range(N):
        for j in range(N):
            if map_pic[i][j] == c:
                y1, x1, y2, x2 = min(y1, i), min(x1, j), max(y2, i), max(x2, j)
                
    color_pos[c] = [y1, x1, y2, x2]

for c, p in color_pos.items():
    for i in range(p[0], p[2]+1):
        for j in range(p[1], p[3]+1):
            if map_pic[i][j] != c:
                check[map_pic[i][j]] = 0

sol = print(sum(check))