import sys
from collections import deque 

def Input_Data():
    readl = sys.stdin.readline
    N, sx, sy = map(int, readl().split())
    paper = [[0] + list(readl().strip()) + [0] if 1 <= r <= N else [0] * (N + 2) for r in range(N + 2)]
    return N, sx, sy, paper
ans = -1
# 입력함수
# N : 모눈종이의 가로 세로 크기
# sx : 특정좌표의 x위치
# sy : 특정좌표의 y위치
# paper : 모눈종이, (0,0)~(N+1,N+1)
N, sx, sy, paper = Input_Data()
 
# 여기서부터 작성
# *:선, .:not 선

dx=[0,1,0,-1]
dy=[1.0,-1,0]

# dfs함수 : 연결된 * 값을 동일한 wall 값으로 변경해주는 함수
def dfs(x,y, table, wall):
    table[x][y] = 1
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 1 <= nx <= n and 1 <= ny <= n and table[nx][ny] == '*':
            dfs(nx, ny, paper)

def dfs_fill(x, y, table, wall, isOutOfRange):
    table[x][y] = wall
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 1 <= nx <= n and 1 <= ny <= n:
            if table[nx][ny] != wall:
                dfs_fill(nx, ny, table, wall, isOutOfRange)
        else:
            isOutOfRange = True
            return

# arrays = []
rec_count = 0
for i in range(1,N+1):
    for j in range(1,N+1):
        if paper[i][j] == '*':
            # array.append([i, j])
            dfs(i, j, paper, rec_count+1)
            rec_count += 1  #단순 직각 다각형 개수 업데이트
            
import copy
sol = 0
for i in range(rec_count):
    isOutOfRange = False
    copied_table = copy.deepcopy(paper)
    dfs_fill(sx, sy, copied_table, i+1, isOutOfRange)

    if isOutOfRange == False:
        sol += 1

print(sol)




# 출력
print(ans)