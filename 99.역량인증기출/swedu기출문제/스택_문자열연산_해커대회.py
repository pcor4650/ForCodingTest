S = list(input())
C = input()

idx = len(S)

for c in C:
    if c == "L" and idx > 0:
        idx -= 1
    if c == "R" and idx < len(S):
        idx += 1
    if c == "B" and idx > 0:
        S.pop(idx -1)
        idx -1
    if ord('a') <= ord(c) <= ord('z'):
        S.append(c)
        idx += 1
print(*S)
        