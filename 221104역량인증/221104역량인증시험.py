221104 역량인증시험

로그인 비번 : zxsd12#

문제1.
===================
조건 :
입력:
0111000
출력 :
0
3
7
8
9

        "111", 	# 정수 0
		"011", 	# 정수 1
		"110", 	# 정수 2
		"111", 	# 정수 3
		"011", 	# 정수 4
		"101", 	# 정수 5
		"101", 	# 정수 6
		"111", 	# 정수 7
		"111", 	# 정수 8
		"111" 

#seg에서 1인 인덱스

given code :
import sys 

def InputData():  
	readl = sys.stdin.readline 
	seg = readl().rstrip()
	return seg

def Solve():
	global sol
	for i in range(0, 10):
		for j in range(0, 7):
			if led[i][j] != seg[j] : break
		else:
			sol[i]=1
			return

def OutputData():
	for i in range(0, 10):
		if sol[i]==1: print(i)

led = [ "1111110", 	# 정수 0
		"0011000", 	# 정수 1
		"0110111", 	# 정수 2
		"0111101", 	# 정수 3
		"1011001", 	# 정수 4
		"1101101", 	# 정수 5
		"1101111", 	# 정수 6
		"0111000", 	# 정수 7
		"1111111", 	# 정수 8
		"1111101" ] # 정수 9 

sol = [0] * 10
seg = InputData()
Solve()
OutputData()

정답 :
===========
import sys 

def InputData():  
	readl = sys.stdin.readline 
	seg = readl().rstrip()
	return seg

def Solve(array):
	global sol
	for i in range(0, 10):
		for j in array:		#i가 0일때 j 1,2,3
			#led[0] = "1111110"
			if led[i][j] != "1" : 
				sol[i] = 0
				break
			else:
				sol[i]=1

def OutputData():
	for i in range(0, 10):
		if sol[i]==1: print(i)

led = [ "1111110", 	# 정수 0
		"0011000", 	# 정수 1
		"0110111", 	# 정수 2
		"0111101", 	# 정수 3
		"1011001", 	# 정수 4
		"1101101", 	# 정수 5
		"1101111", 	# 정수 6
		"0111000", 	# 정수 7
		"1111111", 	# 정수 8
		"1111101" ] # 정수 9 

sol = [0] * 10
seg = InputData()
# print(seg[1])
# print(seg[2])
# print(seg[3])
#seg 값이 1인 모든 인덱스
array = []
for i in range(7):
	if seg[i] == "1":
		array.append(i)

# print(array)
Solve(array)
OutputData()

===========
===================

문제2. 조합
===================
조건 :
3 20
5
7
11
입력 형식 :
첫 번째 줄 : 사다리의 개수N(1~20), 버섯이 있는 곳의 높이 T(모든 사다리 높이의 합)
두번째줄 : N줄에 걸쳐 각 사다리의 높이 H(1~1,000,000)

출력형식
연결한 사다리의 높이의 합과 능이 버섯이 있는 곳의 높이 T와의 차이의 최소값

#접근 방법
1. H배열로 조합 가능한 모든 sumH배열 구하기

2. 그 중에 T보다 큰 배열만 다시 구하기

3. 그 배열 중 최소값 출력

정답 :
import sys
from itertools import combinations

def input_data():
	readl = sys.stdin.readline
	N, T = map(int,readl().split())#사다리의 수, 버섯 채집 지점 높이
	H = [int(input()) for i in range(N)]#각 사다리 높이 저장
	return N, T, H


sol = -1#사다리 높이 합의 버섯 채집 지점 초과 높이

#입력받는 부분
N, T, H = input_data()

#여기서부터 작성
sumH = []

for i in range(1,N+1):
	for x in list(combinations(H,i)):
		sumH.append(sum(x)-T)
# print(sumH)


sumH_overT = [x for x in sumH if x>=0]
# print(sumH_overT)

sol = min(sumH_overT)


#출력하는 부분
print(sol)

===================








문제3. 재귀, 슬라이싱, 리스트 쪼개기, s,e설정?
===================
조건 :
입력 :
7 4 4
3 6 9 12 13 13 15
출력 :
3 3

입력
15 7 5
0 10 100 1000 5000 7000 8000 9000 12000 17000 25000 30000 50000 100000 150000
출력
5000 7

Description :
입력형식 : 
1줄 : 고객수N(1~100,000), 최대 운영 횟수 : K(1~100,000), 접종실 최대 인원M(1~N), N<=K*M
2줄 : 가장 효율적인 방법의 대기시간, 운영횟수 공백 구분 인쇄


7 4 4
A B C  D  E  F  G
3 6 9 12 13 13 15

가장 효율적인 운영방법 :
1. 가장 오래 기다린 고객의 대기시간 최소화
2. 대기시간이 동일한 경우 운영횟수 최소화

     입장 순서  
운영회차    1   2   3   4   대기시간(마지막 입장 고객의 시간 - 처음 입장 고객의 시간)
1회차     A(3)B(6)            3
2회차     C(9)D(12)           3
3회차     E   F   G           2
4회차

given code:
import sys

def input_data():
	readl = sys.stdin.readline
	N, K, M = map(int,readl().split())
	A = list(list(map(int,readl().split())))
	return N, K, M, A


anstime, anscnt = 0, 0
# 입력 함수
N, K, M, A = input_data()

# 여기서부터 작성


# 출력하는 부분
print(anstime, anscnt)
===================

접근방법
1. 고객 예약 시간에 대해 오름차순 sorting 필요
2. 하나의 리스트를 최소 운영횟수 N개로 쪼개는 방법? 슬라이싱?





재귀
7 4 4 -> 최소 운영 횟수 7/4 이상 최소 2번 운영
3 6 9 12 13 13 15
 3 3 3  1  0  2
 
3 6 9 12 | 13 13 15 -> 최대 운영횟수2, 대기시간 9
3 | 6 9 12 | 13 13 15 -> 최대 운영횟수3, 대기시간 6
3 | 6 | 9 12 | 13 13 15 -> 최대 운영횟수4, 대기시간 3
3 | 6 9 | 12 | 13 13 15 -> 최대 운영횟수4, 대기시간 3
3 | 6 9 12 | 13 | 13 15 -> 최대 운영횟수4, 대기시간 6
3 | 6 9 12 | 13 13 | 15 -> 최대 운영횟수4, 대기시간 6

3 6 | 9 12 | 13 13 15 -> 최대 운영횟수3, 대기시간 3
->4가지
3 6 9 | 12 | 13 13 15 -> 최대 운영횟수3, 대기시간 6
3 6 9 12 | 13 |13 15 -> 최대 운영횟수3, 대기시간 9
3 6 9 12 | 13 13 | 15 -> 최대 운영횟수3, 대기시간 9

3 6 9 | 12 13 13 15 -> 최대 운영횟수2, 대기시간 6

출력 :
3 3





입력
15 7 5 -> 최소 운영횟수 3 15/5 부터
0 10 100 1000 5000 | 7000 8000 9000 12000 17000 | 25000 30000 50000 100000 150000  최소운영횟수3, 대기시간 125000
->12가지 방법



출력
5000 7



다른 사람 작성, 답 아님

import sys

def input_data():
	readl = sys.stdin.readline
	N, K, M = map(int,readl().split())
	A = list(list(map(int,readl().split())))
	return N, K, M, A


anstime, anscnt = 0, 0
# 입력 함수
N, K, M, A = input_data()

# 여기서부터 작성
A.sort()
s = 0
e = A[-1] - A[0]

while s<=e:
	mid = (s+e) // 2
	room_cnt = 0
	room = [ [] *M for _ in range(N) ]
	for i in range(N):
		if len(room[room_cnt]) < M:
			room[room_cnt].append(A[i])
		else:
			room_cnt += 1
			room[room_cnt].append(A[i])

		if room[room_cnt][-1] - room[room_cnt][0] > mid:
			room[room_cnt].pop()
			room_cnt += 1
			room[room_cnt].append(A[i])

	if room_cnt >= K:
		s = mid +1
	else:
		e = mid -1
	
# 출력하는 부분
anstime = s
anscnt = room_cnt+1

print(anstime, anscnt)