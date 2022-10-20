import sys

sys.setrecursionlimit(100000)

#상, 하, 좌, 우
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

#x,y 지점을 기준으로 주변을 탐색하는 재귀함수
def sink_DFS(x, y, h):
    #x, y 좌표를 기준으로 상화주우 좌표를 for 문으로 가져옴
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        #nx, ny 좌표에 대한 유효성 검증
        if nx >= 0 and nx < n and ny >= 0 and ny < n :
            if sink_table[nx][ny] == False and water_board[nx][ny] > h: 
                #유효성이 검증된 좌표에 한해 재귀함수를 호출. 이 과정이 없으면 
                sink_table[nx][ny] = True
                sink_DFS(nx, ny, h)
                
n = int(input())
#입력값에 따른 높이 보드 생성
water_board = [list(map(int, input().split())) for _ in range(n)]

ans = 1


for k in range(max(map(max, water_board))): #각 행의 최대값을 map함수를 통해 찾고, 그 값들 중 최대값을 반환 
    sink_table = [[False]*n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if water_board[i][j] > k and sink_table[i][j] == False:
                count += 1
                sink_table[i][j] = True
                sink_DFS(i, j, k)
    ans = max(ans, count)
    
print(ans)



#참고 
# 2차원 리스트를 1차원 리스트로 변환하는 방법?
# list1 = [[1, 10], [2, 22], [3, 19], [4, 7]]
# list2 = sum(list1, [])
# print(list2)

# 결과
# [1, 10, 2, 22, 3, 19, 4, 7]

#2차원 리스트 각 행의 최대값을 찾는 방법?
# map(max, water_board)
