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
for i in range(1, n+1):
    if distance[i] == k :
        print(i)
        check = True

if check == False :
    print(-1)




# 문제
# 입력 조건 :
# 첫째 줄에 도시의 개수 N(2~300,000), 도로의 개수 M(1~1,000,000), 거리정보 K(1~300,000), 출발 도시의 번호 X(1~N)가 주어진다.
# 둘째 줄부터 M개의 줄에 걸쳐서 두 개의 자연수 A, B가 주어지며, 각 자연수는 공백으로 구분한다. 이는 A번 도시에서 B 도시로 이동하는 단방향 도로가 존재한다는 의미입니다.

# 출력 조건 :
# X로부터 출발하여 도달할 수 있는 도시 중에서 최단거리가 K인 모든 도시의 번호를 한 줄에 하나씩 오름차순으로 출력
# 이때 도달할 수 있는 도시 중에서 최단 거리가 K인 도시가 하나도 존재하지 않으면 -1을 출력

# 4 4 2 1
# 1 2
# 1 3
# 2 3
# 2 4
# graph = [[], [2, 3], [3, 4], [], []]

# distance   0  1  2  3  4    -> 0  1  2  3  4   ->    0  1  2  3  4   ->     
#           -1 -1 -1 -1 -1      -1  0 -1 -1 -1        -1  0  1  1 -1