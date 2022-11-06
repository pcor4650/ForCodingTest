n, m = map(int, input().split())
data = []  #초기 맴 리스트
temp = [[0]*m for _ in range(n)]  # 벽을 설치한 뒤의 맵 리스트

for  _ in range(n):
    data.append(list(map(int, input().split())))
    
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

#DFS를 이용해 각 바이러스가 사방으로 퍼지게 하기
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                # 해당위치에 바이러스 값 넣고, 재귀적으로 수행하여 바이러스 퍼지도록
                temp[nx][ny] = 2
                virus(nx, ny)
                
#현재 맵에서 안전 영역의 크기 계산하는 메서드
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

# DFS를 이용해 울타리를 설치하면서, 매번 안전 영역의 크기 계산
def dfs(count):
    global result   #global?
    #울타리가 3개 설치된 경우, temp에 data넣고
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        
        #각 바이러스의 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        #안전 영역의 최대값 계산
        result = max(result, get_score)
        return
    
    #빈 공간에 울타리 설치 => 핵심
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1  #벽 세우기
                count += 1
                dfs(count)  #count가 3이 안되면 재귀적으로 실행하여 벽 세우기
                data[i][j] = 0
                count -= 1
                
dfs(0)
print(result)
    