import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

minSum = 2*1e9
p1, p2 = -1, -1
l, r = 0, N-1

while l < r and minSum != 0:
    val = A[l] + A[r]
    if abs(val) < minSum:
        p1, p2 = l, r
        minSum = abs(val)
    if val < 0:
        l += 1
    else:
        r -= 1
print(p1, p2)