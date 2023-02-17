import sys

input = sys.stdin.readline

N = int(input())
items = []
ids = []
for _ in range(N):
    x, id = map(int, input().split())
    items.append([x, id])
    ids.append(id)

ids = list(set(ids))
ids.sort()
items.sort()

# print(ids)
# print(items)

check = [0]*len(ids)

ans = 2000000001

S = 0
cnt = 0
for E in range(N):
    