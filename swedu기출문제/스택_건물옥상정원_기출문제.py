import sys
read = sys.stdin.readline
N = int(read())
A = []
ans = 0

for i in range(N):
    x = int(input())
    if not A:
        A.append(x)
    else:
        while A and A[-1] <= x:
            A.pop()
        ans += len(A)
        A.append(x)
print(ans)
    