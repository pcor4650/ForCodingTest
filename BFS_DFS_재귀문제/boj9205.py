import sys
input = sys.stdin.readline
from collections import deque

def bfs(start):
    Q = deque()
    Q.append(start)
    while Q:
        x, y = Q.popleft()
        # Q에서 하나씩 꺼내와 endPos와 거리 1000 이내인지 확인
        if abs(endPos[0]-x) + abs(endPos[1]-y) <= 1000:
            print('happy')
            return
        # Q에서 꺼내와 포인트와 방문하지 않은 i번째 편의점과의 거리가 1000 이하이면 Q에 넣기 
        for i in range(n):
            if visited[i] == 0:
                nx, ny = conv[i]
                if abs(nx-x) + abs(ny-y) <= 1000:
                    visited[i] = 1
                    Q.append(conv[i])
    print('sad')
    return       

TC = int(input())
for _ in range(TC):
    n = int(input())
    startPos = list(map(int, input().split()))
    conv = []
    for _ in range(n):
        conv.append(list(map(int, input().split())))
    endPos = list(map(int, input().split()))
    visited = [0]*n
    bfs(startPos)
