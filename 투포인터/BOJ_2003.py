import sys

input = sys.stdin.readline

N, M = map(int, input().split())
Array = list(map(int, input().split()))

cnt = 0
end = 0
interval_sum = 0
for start in range(N):
    while interval_sum < M and end < N:
        interval_sum += Array[end]
        end += 1
    if interval_sum == M:
        cnt += 1
    interval_sum -= Array[start]

print(cnt)











# 입력:
# 4 2
# 1 1 1 1

# 출력 :
# 3