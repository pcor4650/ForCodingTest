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


# 내가 짜본 코드
# n, k = map(int, input().split())

# graph = []
# for _ in range(n):
#     graph.append(list(map(int, input().split())))

# s, x, y = map(int, input().split())

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 0]

# def sol(s, x, y):
#     for _ in range(1, s+1):
#         for i in range(n):
#             for j in range(n):
#                 if graph[i][j] != 0:
#                     for k in range(4):
#                         nx = i + dx[k]
#                         ny = j + dy[k]
#                         if nx >=0 and nx < n and ny >= 0 and ny < n:
#                             if graph[nx][ny] == 0:
#                                 graph[nx][ny] = graph[i][j]
#                             elif graph[nx][ny] != 0 :
#                                 graph[nx][ny] = min(graph[i][j], graph[nx][ny])

# sol(s, x, y)