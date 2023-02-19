import sys
input = sys.stdin.readline

N, S, M = map(int, input().split())

A = list(range(1, N+1))
ans = []
idx = (S-1)%N
while A:
    print("ans: ", ans, ", idx: ", idx, ", len(A): ", len(A))
    idx = (idx -1 + M) % len(A)
    ans.append(A.pop(idx))
# print(" ".join(ans))
print(*ans)