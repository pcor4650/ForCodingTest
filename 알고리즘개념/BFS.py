from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if Visited[i] == False:
                queue.append(i)
                Visited[i] = True
                
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1,7]
]

visited = [False] * 9

bfs(graph, 1, visited)


# FloodFill #
from collections import deque
def solution(n, m, image):
    cnt = 0
    visited = [[False]*m for _ in range(n)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                q = deque()
                q.append([i, j])
                color = image[i][j]
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if 0 <= nx < n and 0 <= ny < n:
                            if not visited[nx][ny]:
                                if image[nx][ny] == color:
                                    visited[nx][ny] = True
                                    q.append([nx, ny])
                cnt += 1
    return cnt
    
# 출처 : https://ygseo.tistory.com/300