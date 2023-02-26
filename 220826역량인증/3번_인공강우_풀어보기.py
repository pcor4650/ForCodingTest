# 인공 강우 생성 횟수 : 6번 이내
# 농장 수 : 10

# 1 1 1 1 1 1 1 ~ 10 10 10 10 10 10 중복조합으로 풀면 경우의 수는 10H6 = (10+6-1)C6 = 5005

# 농장-[x,y,필요강수량] 으로 저장할 딕셔너리 필요, 리스트로 제공해줄 테니 zip() 사용하여 딕셔너리로 변경하는 방법 숙지 필요, 제공 코드 무시하고 직접 만들어도 됨
# 농장-농장에 내린 강우량 저장할 딕셔너리 필요
# 어느 농장에 비를 내릴지에 대해 중복조합 객체 생성
# 농장X에 비가 내렸을 때 유효거리 내 농장에 내린 강우량 업데이트 필요

import sys
input = sys.stdin.readline
from itertools import combinations_with_replacement

N = int(input())
farm_infos = dict()
farmNo = 0
for _ in range(N):
	farmNo += 1
	x, y, need = map(int, input().split())
	farm_infos[farmNo] = [x, y, need]			# 농장_정보 딕셔너리 오케이
M, Q, L = map(int, input().split())

# print(farm_infos)

farm_rainedAmount = dict.fromkeys(farm_infos, 0)
# print(farm_rainedAmount)

twoPoint_dis = dict()
# 농장 간 거리 정보 미리 계산해서 활용
for point1 in farm_infos.keys():
	for point2 in farm_infos.keys():
		if point1 != point2:
			x1, y1, need1 = farm_infos[point1]
			x2, y2, need2 = farm_infos[point2]
			distance = abs(x1-x2)+abs(y1-y2)
			twoPoint_dis[(point1, point2)] = distance
print("twoPoint_dis: ", twoPoint_dis)
# twoPoint_dis:  {(1, 2): 2, (1, 3): 4, (1, 4): 3, (2, 1): 2, (2, 3): 2, (2, 4): 3, (3, 1): 4, (3, 2): 2, (3, 4): 5, (4, 1): 3, (4, 2): 3, (4, 3): 5}

# 1번 농장에 비가 내렸을 때, 몇 번 농장도 같이 비가 내리는지에 대한 데이터 필요
# 1에 내리면 -> 1, 2에 같이 비 내림
# 2에 내리면 -> 1, 2, 3에 같이 비 내림
# 3에 내리면 -> 2, 3에 같이 비 내림
# 4에 내리면 -> 4에만 비 내림

farmNo_farmList = dict()
for twoPoint in twoPoint_dis.keys():
	if twoPoint_dis[twoPoint] <= M:
		p1, p2 = twoPoint
		print("p1: ", p1, "p2: ", p2)


# 어느 농장에 비를 내릴지에 대한 중복조합 생성
whereToRain = combinations_with_replacement(farm_infos.keys(), M)
print("where to rain: ", list(whereToRain))

# 각각의 중복조합 케이스에 대해 농장에 비가 얼마나 내렸는지 업데이트
# 유효거리 내의 농장을 어떻게 찾지?
# for eachCase in whereToRain:
# 	for rainedFarm in eachCase:
		





# 입력 :
# 4
# 1 1 60
# 1 3 100
# 1 5 90
# 3 2 40
# 2 50 2

# 결과 :
# 3