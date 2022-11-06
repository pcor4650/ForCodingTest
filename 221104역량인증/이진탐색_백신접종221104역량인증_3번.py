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

s = 0               # 한 접종실 당 한명의 인원이 있을 경우
e = A[-1] - A[0]    # 한 접종실에 모든 인원이 있을 경우

while s<=e:
	mid = (s+e) // 2
	room_cnt = 0
	room = [ [] *M for _ in range(N) ]		
	for i in range(N):
		if len(room[room_cnt]) < M:                 # 접종실 안의 인원수가 M보다 작다면 접종실에 인원 추가
			room[room_cnt].append(A[i])     
		else:
			room_cnt += 1                           # 접종실 내 인원이 M 이상이면 다음 접종실에 인원 추가
			room[room_cnt].append(A[i])

		if room[room_cnt][-1] - room[room_cnt][0] > mid:    # 접종실의 마지막 인원의 예약시간과 처음 인원의 예약시간 차이가 기준값보다 크면
			room[room_cnt].pop()                            # 마지만 원소 빼서   
			room_cnt += 1
			room[room_cnt].append(A[i])                     # 그 다음 접종실에 추가

	if room_cnt + 1 >= K:
		s = mid +1
	else:
		e = mid -1
	
# 출력하는 부분
anstime = s
anscnt = room_cnt+1

print(anstime, anscnt)


# Description :
# 입력형식 : 
# 1줄 : 고객수N(1~100,000), 최대 운영 횟수 : K(1~100,000), 접종실 최대 인원M(1~N), N<=K*M               7 4 4
# 2줄 : 가장 효율적인 방법의 대기시간, 운영횟수 공백 구분 인쇄                                              3 6 9 12 13 13 15  -> 정렬 필요

# 7 4 4
# A B C  D  E  F  G
# 3 6 9 12 13 13 15

# 가장 효율적인 운영방법 :
# 1. 가장 오래 기다린 고객의 대기시간 최소화
# 2. 대기시간이 동일한 경우 운영횟수 최소화

#      입장 순서  
# 운영회차    1   2   3   4   대기시간(마지막 입장 고객의 시간 - 처음 입장 고객의 시간)
# 1회차     A(3)B(6)            3
# 2회차     C(9)D(12)           3
# 3회차     E   F   G           2
# 4회차