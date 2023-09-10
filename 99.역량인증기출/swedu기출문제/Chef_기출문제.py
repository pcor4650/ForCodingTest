import sys


def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	TP = []
	maxT = 0
	for _ in range(N):
		p, t = map(int, input().split())
		maxT = max(maxT, t)
		TP.append([t, p])
	TP.sort()

	return N, TP, maxT

# 입력
# N : 손님 수
# P : 음식 값
# T : 예약 희망 시간
N, TP, maxT = Input_Data()

# 코드를 작성하세요
profit = 0
S = [0]*(maxT+1)
store = []
for t in reversed(range(1, maxT+1)):
		# print(i)
	while TP and TP[-1][0] >= t:
		store.append(TP.pop()[1])
	if store:
		store.sort()
		S[t] = store.pop()
	else:
		S[t] = 0
print(sum(S))


# 출력
# print(maxT)
# print(TP.pop()[1])
