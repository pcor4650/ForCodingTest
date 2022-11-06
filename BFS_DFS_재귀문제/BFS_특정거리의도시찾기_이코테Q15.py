from collections import deque

# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시 번호 입력받기
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]  # 왜 이렇게 만들어 줄까?

# 모든 도로 정보 입력받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)  # 여기가 핵심인듯

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (n+1)
distance[k] = 0  # 출발도시까지의 거리는 0으로

# 너비 우선 탐색 수행
q = deque([x])
while q:
    now = q.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시 확인
    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)

# 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in rnage(1, n+1):
    if distance[i] == k :
        print(i)
        check = True

if check == False :
    print(-1)