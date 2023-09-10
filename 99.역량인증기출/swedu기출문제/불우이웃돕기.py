import sys

input = sys.stdin.readline

N = int(input())
units = [1, 5, 10, 50, 100, 500, 1000, 3000, 6000, 12000]
Boxs = list(map(int, input().split()))

sum_Boxs = []
for i in range(len(units)):
    if i == 0:
        sum_Boxs.append(units[i] * Boxs[i])
    else:
        sum_Boxs.append(sum_Boxs[-1] + units[i] * Boxs[i])

# print(sum_Boxs)

# 1, 5,  10, 50, 100, 500, 1000, 3000, 6000, 12000
# 3  3    3   3   3    3    3     3     3      3
# 3  18  48  ...

for i in range(len(sum_Boxs)):
    if sum_Boxs[i] >= N:
        index = i
        break
# print(index)

send_Boxs = [0]*len(units)

for i  in range(index, -1, -1):
    if i == 0:
        send_Boxs[0] = N
    # print("i: ", i, ", N: ", N, ", sum_Boxs[i]: ", sum_Boxs[i], ", Boxs[i]: ", Boxs[i])
    while N > sum_Boxs[i-1] and Boxs[i] > 0:
        # print("i: ", i, ", N: ", N, ", sum_Boxs[i]: ", sum_Boxs[i], ", Boxs[i]: ", Boxs[i])
        N -= units[i]
        Boxs[i] -= 1
        send_Boxs[i] += 1

print(sum(send_Boxs))
print(*send_Boxs)