import sys

input = sys.stdin.readline

N, K = map(int, input().split())
tmps = list(map(int, input().split()))

window = K

max_sum = (-100) * K
part_sum = sum(tmps[0:window])
max_sum = max(max_sum, part_sum)
for s in range(1, N-window+1):
    part_sum = part_sum - tmps[s-1] + tmps[s+window-1] 
    # print("s: ", s, ", part_sum: ", part_sum, ", max_sum: ", max_sum)
    max_sum = max(max_sum, part_sum)

print(max_sum)
