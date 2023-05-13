# oasis = [int(input()) for _ in range(int(input()))]

# stack = [] # (키, cnt)로 append
# result = 0

# for o in oasis:

#   # 스택 끝 값보다 키 크면 pop
#   while stack and stack[-1][0]<o:
#     result += stack.pop()[1]

#   # 스택이 비어있으면 해당 키 append하고 continue
#   if not stack:
#     stack.append((o, 1))
#     continue

    
#   # 스택 끝 값의 키와 같을 때
#   if stack[-1][0]==o:
#     cnt = stack.pop()[1]
#     result += cnt

#     if stack: result += 1
#     stack.append((o, cnt+1))

#   # 스택 끝 값의 키보다 작을 때
#   else:
#     stack.append((o, 1))
#     result += 1

# # 결과값 출력
# print(result)


import sys

N = int(sys.stdin.readline())
heights = []
answer = 0
stack = []

for _ in range(N):
    height = int(sys.stdin.readline())
    heights.append(height)

    while stack and stack[-1][0] <= height:
        h, cnt = stack.pop()
        answer += cnt

        if h == height:
            answer += 1

    stack.append((height, answer))
    answer = 0

print(sum(item[1] for item in stack))
