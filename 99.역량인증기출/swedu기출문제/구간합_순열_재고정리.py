# 입력 : 
# 7 2
# 1 2 2 2 1 2 1
# 1 : 3개, 2 : 4개

# from itertools import permutations

# N, M = map(int, input().split())
# A = list(map(int, input().split()))
# num = [0]*10
# psum = [[0 for _ in range(N+1)] for _ in range(M+1)]

# for i, a in enumerate(A):
#     num[a] += 1
#     for b in range(1, M+1):
#         psum[b][i+1] = psum[b][i]
#         if a == b:
#             psum[b][i+1] += 1

# total = 0
# for P in permutations(range(1,M+1)):
#     idx = 0
#     cnt = 0
#     for p in P:
#         s,e = idx, idx+num[p]
#         cnt += psum[p][e]-psum[p][s]
#         idx = e
#     total = max(total, cnt)
# print(N-total)

import sys
input = sys.stdin.readline
from itertools import permutations

N, M = map(int, input().split())
A = list(map(int, input().split()))
num = [0]*10
psum = [[0]*(N+1) for _ in range(M+1)]

for i, a in enumerate(A):
    num[a] += 1
    for b in range(1, M+1):
        psum[b][i+1] = psum[b][i]
        if a == b:
            psum[b][i+1] += 1

total = 0
print("permutations(range(1, M+1)) : ", list(permutations(range(1, M+1))))
for P in permutations(range(1, M+1)):
    idx = 0
    cnt = 0
    for p in P:
        print("p: ", p)
        s, e = idx, idx+num[p]
        cnt += psum[p][e]-psum[p][s]
        idx = e
        print("s: ", s, ", e: ", e, ", cnt: ", cnt)
    total = max(total, cnt)
print(N-total)


# 풀이 방법
# 주어진 배열 : 	    1 2 2 2 1 2 1
# 1이 있는 배열 접두합 :0 1 1 1 1 2 2 3
# 2가 있는 배열 접두합 :0 0 1 2 3 3 4 4 