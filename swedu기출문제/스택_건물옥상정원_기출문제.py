# 내 건물이 보이는 옥사의 수 계산

# stack = []	[5]		[5, 2]		[5]    [5, 4]		[5, 4]  [5,4,3]  		[5, 4] [5] []  [6]  		[6, 1]
# cnt = 0			 0		   1  		 1        2	 		  4              		                    		  5

import sys

input = sys.stdin.readline

N = int(input())
Heights = []
for _ in range(N):
	Heights.append(int(input()))

stack = []
cnt = 0

for height in Heights:
	if not stack:
		stack.append(height)	
	else:
		while stack and stack[-1] <= height:
			stack.pop()
		cnt += len(stack)
		stack.append(height)

print(cnt)
print(stack)