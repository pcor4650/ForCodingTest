import sys
input = sys.stdin.readline

N = int(input())
datas = list(map(int, input().split()))
datas.sort()    # -99 -2 -1 4 98

start = 0
end = N-1

ans = abs(datas[start] + datas[end])
final = [datas[start], datas[end]]

while start < end:
    left_val = datas[start]
    right_val = datas[end]
    tmp_sum = left_val + right_val
    if abs(tmp_sum) < ans:
        ans = abs(tmp_sum)
        final = [left_val, right_val]
        if ans == 0:
            break
    if tmp_sum < 0:
        start += 1
    else:
        end -= 1

a, b = final
print(a, b)