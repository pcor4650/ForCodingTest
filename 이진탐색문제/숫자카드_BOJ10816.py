import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right

N = int(input())
player_card = list(map(int, input().split()))
M = int(input())
check_card = list(map(int, input().split()))

player_card.sort()

# print(player_card)

# value가 array에서 몇개 있는지 확인을 위한 함수, array는 정렬되어 있어야 
def count_by_range(array, value):
    right_index = bisect_right(array, value)
    left_index = bisect_left(array, value)
    return right_index - left_index

cnt = []
for card in check_card:
    cnt.append(count_by_range(player_card, card))

print(*cnt)