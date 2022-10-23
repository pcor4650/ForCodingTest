import sys
 
def InputData():
    readl = sys.stdin.readline
    N = int(readl())
    D = [list(map(int,readl().split())) for r in range(N)]
    return N, D
 
 
ans = -1
# 입력 함수
N, D = InputData()
# 여기서부터 작성

# 상 하 좌 우
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 정사각이 아닐 경우
# h = len(D)
# w = len(D[0])

#군락 카운트 위해
def DFS(x, y, field, minAge):
    field[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and field[nx][ny] > minAge:
            DFS(nx, ny, field, minAge)

count = 0

#나무 생육일수 정렬
ageList = []
for i in range(n):
    for j in range(n):
        ageList.append(D[i][j])
        
uniqueAge = list(set(ageList))
uniqueAge.sort()

idx = 0
maxGroups = 0
maxGroupsAge = 0

import copy
for age in uniqueAge:
    # 2차원 이상 배열은 copy()를 하면 내용복사가 안되므로 deepcopy 이용
    filed = copy.deepcopy(D)    # 매 for문 마다 field 값 초기화, deepcopy 없이 다른 방법은?
    count = 0   # 매 for문 마다 count 값 초기화
    for i in range(n):
        for j in range(n):
            if filed[i][j] > age:
                DFS(i, j, field, age)
                count += 1
    if count > maxGroups:
        maxGroups = count
        maxGroupsAge = age
    
#잘려진 나무의 개수 구하기
cutCnt = 0
for i in range(n):
    for j in range(n):
        if D[i][j] <= maxGroupsAge:
            cutCnt += 1
            
print(cutCnt)
