# import sys
# input = sys.stdin.readline
# n = int(input())
# oasis = [int(input()) for _ in range(n)]

# stack = []
# result = 0

# for o in oasis:
#     while stack and stack[-1][0] < o:
#         result += stack.pop()[1]

#     if not stack:
#         stack.append((o, 1))
#         continue

#     if stack[-1][0] == o:
#         cnt = stack.pop()[1]
#         result += cnt

#         if stack:
#             result += 1
#         stack.append((o, cnt+1))
#     else:
#         stack.append((o, 1))
#         result += 1

# print(result)

import sys
input = sys.stdin.readline
n = int(input())
oasis = [int(input()) for _ in range(n)]

stack = []
result = 0

for o in oasis:
    cnt = 1

    while stack and stack[-1][0] <= o:
        if stack[-1][0] == o:
            cnt += stack[-1][1]
        result += stack.pop()[1]

    if stack:
        result += 1
    stack.append((o, cnt))

print(result)
