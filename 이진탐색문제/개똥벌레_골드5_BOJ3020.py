import sys
input = sys.stdin.readline
from bisect import bisect_left

N, H = map(int, input().split())
cave = [int(input().rstrip()) for _ in range(N)]

top, bot = [], []
for i in range(N):
    if i%2 == 0:
        bot.append(cave[i])
    else:
        top.append(cave[i])

top.sort()
bot.sort()
cnt = 1

min_val = N


print("top: ", top)
print("bot: ", bot)

for h in range(1, H+1):
    t, b = bisect_left(top,  (H+1)-h), bisect_left(bot, h)
    total = N-(t+b)
    print("h: ", h, ", t:", t, ", b: ", b, ", total:", total, ", min_val: ", min_val)
    if total < min_val:
        min_val = total
        cnt = 1
    elif total == min_val:
        cnt += 1
print(min_val, cnt)