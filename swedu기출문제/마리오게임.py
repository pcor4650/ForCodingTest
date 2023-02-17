import sys

input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))
maxS = [0]*N
# print(maxS)

for i in range(N):
    if i == 0:
        maxS[i] = P[i]
    else:
        if P[i-1] < P[i]:
            maxS[i] = maxS[i-1] + (P[i] - P[i-1])
        else:
            maxS[i] = maxS[i-1]
print(maxS[-1])    


#i      0 1 2  3   4   5  6  7
#P      7 2 1  8   4   3  5  6
#maxS   7 7 7 14  14  14 16 17
# 점화식 : (조건1) maxS[i] = maxS[i-1] + (P[i] - P[i-1]) or (조건2) maxS[i] = maxS[i-1]