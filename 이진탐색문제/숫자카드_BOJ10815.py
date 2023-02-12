import sys
input = sys.stdin.readline

N = int(input())
player_card = list(map(int, input().split()))
M = int(input())
check_card = list(map(int, input().split()))

player_card.sort()

check = []
for card in check_card:
    c = 0
    start, end = 0, N-1
    while start <= end:
        mid = (start + end) // 2
        # print("s: ", start, ", e: ", end, ", m:", mid, ", card: ", card, ", player_card[mid]: ", player_card[mid])
        if player_card[mid] <= card:
            start = mid + 1
            if player_card[mid] == card:
                c = 1
        elif player_card[mid] > card:
            end = mid - 1

    check.append(c)

print(*check)