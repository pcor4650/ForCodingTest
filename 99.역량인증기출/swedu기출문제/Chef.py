# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# user_input = input()
# print ("Hello Goorm! Your input is " + user_input)

# N = int(input())
# A = list()
# maxt = 0

# for _ in range(N):
# 	p, t = map(int, input().split())
# 	maxt = max(maxt, t)
# 	A.append([t, p])
# A.sort()

# # print("maxt: ",maxt)
# # print(A)

# ans = 0
# S = list()
# for t in reversed(range(1,maxt+1)):
# 	# print("A: ", A, ", A[-1][0]: ",A[-1][0], ", t:", t, ", A and A[-1][0]",A and A[-1][0])
# 	while A and A[-1][0] >= t:
# 		S.append(A.pop()[1])
# 		# print("S: ",S)
# 	if S:
# 		m = max(S)
# 		ans += m
# 		S.remove(m)
# print(ans)



#시간초과
# N = int(input())
# A = [list(map(int,input().split())) for _ in range(N)]
 
# #print(A)
# check = [0]*10010
 
# for i in range(N):
#     P, T = A[i]
#     #print(P,T)
#     while T > 0:
#         if check[T] == 0:
#             check[T] = P
#             break
#         else:
#             if check[T] < P:
#                 P, check[T] = check[T], P
#             T -= 1
# print(sum(check))

import sys

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	TP = []
	maxT = 0
	for _ in range(N):
		p, t = map(int, input().split())
		TP.append([t, p])
		maxT = max(maxT, t)
	# PT = [list(map(int,readl().split())) for _ in range(N)]
	# P = [x[0] for x in PT]
	# T = [x[1] for x in PT]
	return N, TP, maxT


# 입력
# N : 손님 수
# P : 음식 값
# T : 예약 희망 시간
N, TP, maxT = Input_Data()

# 코드를 작성하세요
TP.sort()
# print(TP)
maxP = 0
S = []	# 왜 필요?
for t in range(maxT, 0, -1):
	# print("t: ", t)
	while TP and TP[-1][0] >= t:
		# print("t: ", t, ", TP[-1][0]: ", TP[-1][0])
		S.append(TP.pop()[1])
	if S:
		m = max(S)
		maxP += m
		S.remove(m)

# 출력
print(maxP)