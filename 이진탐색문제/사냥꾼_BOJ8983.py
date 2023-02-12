import sys
input = sys.stdin.readline

M, N, L = map(int, input().split())
pos_M = list(map(int, input().split()))
pos_N = []
for _ in range(N):
    x, y = map(int, input().split())
    pos_N.append([x,y])

#여기서 부터 코드 입력
pos_M.sort()
cnt = 0

for x, y in pos_N:
    start, end = 0, M-1
    while start < end:
        mid = (start + end) // 2
        # print("start:", start, ", end:", end, ", mid:", mid)
        
        if pos_M[mid] < x:
            start = mid + 1
        elif pos_M[mid] > x:
            end = mid - 1
        else:
            start = mid
            break
    # print("start:", start, "pos_M[start]: ", pos_M[start])
    if abs(pos_M[start] - x) + y <= L:
        cnt += 1
    elif start+1 < M and abs(pos_M[start+1] - x) + y <= L:
        cnt += 1
    elif start > 0 and abs(pos_M[start-1] - x) + y <= L:
        cnt += 1
    # print("cnt:", cnt)
print(cnt)