n = int(input())
A = []
maxT = 0

for _ in range(n):
    p, t = list(map(int, input().split()))
    maxT = max(maxT, t)
    A.append([t,p])
A.sort()

ans = 0
S = [0]*(maxT+1)

store = []
for t in reversed(range(1,maxT+1)):
    while A and A[-1][0] >= t:
        store.append(A.pop()[1])
    store.sort()
    S[i] = store.pop()
    
print(sum(S))