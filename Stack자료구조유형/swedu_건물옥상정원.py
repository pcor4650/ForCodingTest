import sys
input = sys.stdin.readline

N = int(input())
buildings = [int(input()) for _ in range(N)]

stack = []
cnt = 0

for building in buildings:
    while stack and stack[-1] <= building:
        stack.pop()
    cnt += len(stack)
    stack.append(building)

print("cnt:", cnt)