import sys


def InputData():
	readl = sys.stdin.readline
	N, K = map(int,readl().split())
	X = [int(readl()) for r in range(N)]
	return N, K, X

ans = -1
# 입력 함수
##N : 이물질의 개수
##K : 장비 최대 사용가능 횟수
##X : 이물질의 위치
N, K, X = InputData()
# 여기서부터 작성
X.sort()
s = 1
e = X[N-1]

while s <= e :
	cnt = 1
	mid = (s+e)//2
	fEle = X[0]
	# print("===")
	# print("s:", s, "e:", e, "mid:", mid, "fEle:", fEle)
	for i in range(1, N):
		# print("s:", s, "e:", e, "mid:", mid, "fEle:", fEle, "cnt:", cnt )
		if X[i] <= fEle + 2*mid:
			continue
		else:
			fEle = X[i]
			cnt += 1
	
	if cnt <= K:
		e = mid - 1
	else :
		s = mid + 1
			
		

# 출력
print(s)




# 풀이
# 3번) 이진탐색으로
# s = 1, e = 24
# 흡입력 V * 2 범위
# 흡입력을 높이고 낮추며 탐색 필요

# 이물질 위치 : [1, 3, 8, 10, 18, 20, 25]

# 1 + 5*2 = 11까지 청소가능
# 	cnt + 1
# 18 + 5*2 = 28까지 청소 가능
# 	cnt + 1

# 입력 : 
# N K
# N줄에 걸쳐 이물질 위치 x