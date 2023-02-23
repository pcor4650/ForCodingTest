import sys

input = sys.stdin.readline

W, H = map(int, input().split())
cnt = int(input())
x, y = [0, W], [0, H]
for _ in range(cnt):
    wh, pos = map(int, input().split())
    if wh == 0:
        y.append(pos)
    else:
        x.append(pos)
x.sort()
y.sort()

w, h = [], []
for i in range(len(x) - 1):
    d= x[i+1]-x[i]
    w.append(d)
w.append(x[0])
    
for i in range(len(y) - 1):
    d= y[i+1]-y[i]
    h.append(d)

maxW, maxH = max(w), max(h)

print(maxW*maxH)
