import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())

def bfs(N, K):
    q = deque()
    q.append([N, 0])
    visited = set([N])

    while q:
        curr, cnt = q.popleft()

        if curr == K:
            return cnt
        
        for move in [curr-1, curr+1, curr*2]:
            if 0<=move<=100000 and move not in visited:
                q.append([move, cnt+1])
                visited.add(move)

print(bfs(N,K))