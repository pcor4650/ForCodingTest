# 인공 강우 생성 횟수 : 6번 이내
# 농장 수 : 10

# 1 1 1 1 1 1 1 ~ 10 10 10 10 10 10 중복조합으로 풀때 최악의 경우의 수는 10H6 = (10+6-1)C6 = 5005

# 농장-[x,y,필요강수량] 으로 저장할 딕셔너리 필요, 리스트로 제공해줄 테니 zip() 사용하여 딕셔너리로 변경하는 방법 숙지 필요, 제공 코드 무시하고 직접 만들어도 될듯
# 농장-농장에 내린 강우량,  저장할 딕셔너리 필요
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
farmsList = list(farm_infos)

twoPoint_dis = dict()
# 농장 간 거리 정보 미리 계산해서 활용
for point1 in farm_infos.keys():
	for point2 in farm_infos.keys():
		# if point1 != point2:
		x1, y1, need1 = farm_infos[point1]
		x2, y2, need2 = farm_infos[point2]
		distance = abs(x1-x2)+abs(y1-y2)
		twoPoint_dis[(point1, point2)] = distance
# print("twoPoint_dis: ", twoPoint_dis)
# twoPoint_dis:  {(1, 1): 0, (1, 2): 2, (1, 3): 4, (1, 4): 3, (2, 1): 2, (2, 2): 0, (2, 3): 2, (2, 4): 3, (3, 1): 4, (3, 2): 2, (3, 3): 0, (3, 4): 5, (4, 1): 3, (4, 2): 3, (4, 3): 5, (4, 4): 0}


# Farm에 비가 내릴 때 유효 거리 내에 모든 농장 내린 비 업데이트
def updateRainedStatusForEachFarm(Farm):
	for f in farm_infos.keys():
		if twoPoint_dis[(f, Farm)] <= L:
			farm_rainedAmount[f] += Q


# 어느 농장에 비를 내릴지에 대한 중복조합 생성
whereToRain = combinations_with_replacement(farm_infos.keys(), M)
# print("where to rain: ", list(whereToRain))
# where to rain:  [(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]

# 각각의 중복조합 케이스에 대해 농장에 비가 얼마나 내렸는지 업데이트
maxCnt = 0
for eachCase in whereToRain:
	farm_rainedAmount = dict.fromkeys(farm_infos, 0)
	tmpCnt = 0
	# print(farm_rainedAmount)
	for f in eachCase:
		updateRainedStatusForEachFarm(f)
	for farm in farmsList:
		x, y, need = farm_infos[farm]
		if farm_rainedAmount[farm] >= need:
			tmpCnt += 1
	maxCnt = max(maxCnt, tmpCnt)

print(maxCnt)


# 입력 :
# 4
# 1 1 60
# 1 3 100
# 1 5 90
# 3 2 40
# 2 50 2

# 결과 :
# 3