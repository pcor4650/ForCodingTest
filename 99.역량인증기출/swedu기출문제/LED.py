import sys
input = sys.stdin.readline

N = int(input())
S = list(map(int, input().split()))
pre = S[0]
cnt = 1
part_S = []

for i in range(1, N):
    if S[i] != pre:
        cnt += 1        
    else:
        part_S.append(cnt)
        cnt = 1
    pre = S[i]
part_S.append(cnt)

sol = 0
# print(part_S)
if len(part_S) <= 3:
    print(N)
else:
    for i in range(2, len(part_S)):
        # print("i: ", i, ", part_S[i-2:i+1]: ", part_S[i-2:i+1])
        sol = max(sol, sum(part_S[i-2:i+1]))
    print(sol)