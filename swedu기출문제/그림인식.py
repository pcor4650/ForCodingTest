import sys

input = sys.stdin.readline

N = int(input())
board = []
color = set()

for _ in range(N):
    tmp = input().strip()
    for c in tmp:
        if c != "0":
            color.add(c)
    board.append(tmp)

pos = dict()
for c in color:
    y1, x1, y2, x2 = 11, 11, -1, -1
    for i in range(N):
        for j in range(N):
            if board[i][j] == c:
                y1, x1, y2, x2 = min(y1, i), min(x1, j), max(y2, i), max(x2, j)
    pos[c] = [y1, x1, y2, x2]

check = [0 for _ in range(10)]

for i in color:
    check[int(i)] = 1
    
print("pos.items(): ", pos.items())

for k,v in pos.items():
    for i in range(v[0], v[2]+1):
        for j in range(v[1], v[3]+1):
            if board[i][j] != 0 and board[i][j] != k:
                check[int(board[i][j])] = 0
print(sum(check))
