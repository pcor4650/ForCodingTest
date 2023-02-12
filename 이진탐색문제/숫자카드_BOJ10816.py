import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right

N = int(input())
player_card = list(map(int, input().split()))
M = int(input())
check_card = list(map(int, input().split()))

player_card.sort()

# print(player_card)

def count_by_range(array, value):
    right_index = bisect_right(array, value)
    left_index = bisect_left(array, value)
    return right_index - left_index

cnt = []
for card in check_card:
    cnt.append(count_by_range(player_card, card))

print(*cnt)