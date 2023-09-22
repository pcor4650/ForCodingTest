import copy
import sys
from collections import deque


def InputData():
	readl = sys.stdin.readline
	S, E1, E2 = map(int, readl().split())
	return S, E1, E2

ans1 = 0
ans2 = 0

# 입력받는 부분
S, E1, E2 = InputData()

# 여기서부터 작성
# 약수 개수 구하는 함수, 이걸 해야 시간 초과 발생 막을 수 있다
def CalNumberOfFactor(number):
    cnt = 0
    sqrt_number = int(number**0.5) + 1  # 루트를 활용하여 범위 최적화
    for i in range(1, sqrt_number):
        if number % i == 0:
            cnt += 1
            if i != number // i:  # 중복 카운트 방지
                cnt += 1
    return cnt


# 4자리 숫자의 각 자리의 숫자를 구하는 함수
def eachDigitNumber(number):
	a = (number // 1000) % 10
	b = (number // 100) % 10
	c = (number // 10) % 10
	d = (number // 1) % 10
	return [a, b, c, d]

def bfs(start, end):
	Q = deque()
	Q.append([start, 0])		#위치, 약수의 개수, cnt
	setPos = set()
	while Q:
		pos, cnt = Q.popleft()
		setPos.add(pos)
		if pos == end:
			return cnt
		# 다음위치 표시하는 For loop
		pos_eachNumber = eachDigitNumber(pos)
		for i in range(4):
			for d in range(10):
				newPosList = copy.deepcopy(pos_eachNumber)
				if newPosList[i] != d:
					newPosList[i] = d
					newPos = 	newPosList[0]*1000 + newPosList[1]*100 + newPosList[2]*10 + newPosList[3]
				
					if  abs(CalNumberOfFactor(pos)-CalNumberOfFactor(newPos)) <= 1 and newPos not in setPos:
					
						setPos.add(newPos)   # 요거 빼먹었었네
						Q.append([newPos, cnt+1])
						# print("newPos: ", newPos, "약수개수:", CalNumberOfFactor(newPos), "cnt: ", cnt)

# print("sol:", bfs(2023, 2123))

# 출력하는 부분
print(bfs(S,E1))
print(bfs(S,E2))




# 2번) 출발행성 -> 목적행성으로 이동
# 풀이방법 : BFS

# 4자리수에서 한 자리만 바꾼 수 : 9*4 = 36개, 한 자리 숫자만 바꾸는 함수????
# 숫자가 주어졌을 때 약수의 개수를 구하는 함수 : 함수로

# 입력 : 
# 2023 2225 2123

# 2023 -> 2225 : 3번
# Q = (2023, 0)
# Q = ((2523, 1)...)
# Q = (2525, 2) ...
# == 2225, cnt 출력

# 2023 -> 2123 : 8번