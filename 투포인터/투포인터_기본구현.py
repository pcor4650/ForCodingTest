n = 5   # 데이터의 개수
m = 5   # 찾고자 하는 부분합
data = [1, 2, 3, 4, 5]

# data 의 부분합이 5가 되는 경우의 수 개수 구하기

cnt = 0
interval_sum = 0
end = 0

for start in range(n):
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    if interval_sum == m:
        cnt += 1
    interval_sum -= data[start]

print(cnt)

#############################################################################

