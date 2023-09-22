from collections import deque

n, k = map(int, input().split())
graph = []
data = [] #바이러스에 대한 정보를 담는 리스트, 왜필요?

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        #해당 위치에 바이러스가 존재하는 경우
        if graph[i][j] != 0:
            #(바이러스 종료, 시간, 위치x, 위치y) 삽입
            data.append((graph[i][j], 0, i, j))     #핵심 코드

#정렬 이후에 큐로 옮기기(낮은 번호의 바이러스가 먼저 증식하므로
data.sort()
q = deque(data)
print(q)
q.popleft()
print(q)

target_s, target_x, target_y = map(int, input().split())

#바이러스가 퍼져나갈 수 있는 4가지 위치
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

#BFS 진행
while q:
    virus, s, x, y = q. popleft() 
    if s == target_s:
        break
    #현재 노드에서 주변 4가지 위치를 각각 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        #nx, ny가 정상 범위에 있는 경우
        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            #아직 방문하지 않은 위차라면, 그 위치에 바이러스 넣기
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s+1, nx, ny))

print(graph[target_x-1][target_y-1])   #출력할때도 주의!


# 문제
# 입력조건 : 
# 첫째 줄에 자연수 N(1~200), K(1~1000)가 주어지며, 각 자연수는 공백으로 구분
# 둘째 줄부터 N개의 줄에 걸쳐 시험관의 정보가 주어진다. 바이러스가 존재하지 않는 경우 0, 존재하면 각 바이러스 번호가 입력
# N+2 번째 줄에는 S(1~10,000), X, Y가 주어지며 공백으로 구분

# 3 3
# 1 0 2   ->   1 1 2   ->   1 1 2        
# 0 0 0        1 0 2        1 1 2
# 3 0 0        3 3 0        3 3 2
# 2 3 2

# data = [(1, 0, 0, 0), (2, 0, 0, 2), (3, 0, 2, 0)]   (바이러스종류, 시간, x, y)