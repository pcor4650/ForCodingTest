import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
a , b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [-1 for _ in range(n+1)]

# tip : 두 포인트 간 거리가 제공되면 (n+1) x (n+1) 행렬 안에 각각 연결된 항목 저장
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(curr_node):
    q = deque()
    q.append(curr_node)
    while q:
        node = q.popleft()
        for i in graph[node]:
            if visited[i] == -1:
                visited[i] = visited[node]+1
                q.append(i)
visited[a] = 0
bfs(a)
print(visited[b])
