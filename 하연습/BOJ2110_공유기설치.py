import sys

input = sys.stdin.readline

N, C = map(int, input().split())
A = []
for _ in range(N):
    A.append(int(input()))
A.sort()

s = 1
e = A[-1] - A[0]

while s<=e:
    m = (s+e)//2
    # print("s: ", s, "m: ", m, "e: ", e)
    pre = A[0]
    cnt = 1
    
    for i in range(1, len(A)):
        if A[i] - pre >= m:
            cnt += 1
            pre = A[i]
    if cnt < C:
        e = m-1
        
    else:
        s = m+1   
print(e)