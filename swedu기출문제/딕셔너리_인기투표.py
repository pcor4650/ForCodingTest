# # -*- coding: utf-8 -*-
# # UTF-8 encoding when using korean
# # user_input = input()
# # print ("Hello Goorm! Your input is " + user_input)

N = int(input())
A = list(input().split())
SC = dict()
for name in A:
	SC[name] = 0
# print(SC)
	
M = int(input())
for _ in range(M):
	name, s = input().split()
	score = int(s)
	if SC.get(name, -1) != -1:
		SC[name] += score
# print(SC)

SC_list = list(SC.items())
SC_list.sort(key=lambda x:-x[1])
# print(SC_list)

for i in range(3):
	print(SC_list[i][0], SC_list[i][1])

# B = []
# for i,name in enumerate(A):
# 	B.append([i, SC[name]])
# B.sort(key=lambda x: [-x[1], x[0]])
# # print(B)
# for i in range(3):
# 	print(A[B[i][0]], B[i][1])


