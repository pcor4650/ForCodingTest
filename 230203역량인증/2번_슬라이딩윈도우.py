import sys


def Input_Data():
	readl = sys.stdin.readline
	N, s, e = map(int, readl().split())
	R = list(map(int,readl().split()))
	return N, s, e, R

# N : 손익 금액의 개수
# s, e : 기간의 범위
# R : 손익 금액
N, s, e, R = Input_Data()#입력받는 부분

# sol = -1
	
#코드를 작성하시오



#출력하는 부분
# print(sol)


# 입력 : 
# 5 1 2   5개 손익, 1~2일간의 인터벌 합이 가작 작은
# 3 -1 -2 3 1

# s              s                 s              s                 s              s
# 3 -1 -2 3 1 -> 3 -1 -2 3 1 -> 3 -1 -2 3 1 -> 3 -1 -2 3 1 -> 3 -1 -2 3 1 -> 3 -1 -2 3 1 
# e                 e              e                 e              e                e
# min_sum: 
# 3              2                 -1             -3                -2              1

# sums = []
min_sum = 100000000

for start in range(N):
	end = start + s -1
	interval_sum = sum(R[start:end+1])
	min_sum = min(interval_sum, min_sum)
	while end - start  <= e - 1 and end <= N-1:
		end += 1
		interval_sum = sum(R[start:end+1])
		min_sum = min(interval_sum, min_sum)
	
# print("R[0:1]",(R[0:1])	)
	


# for i in range(s, e+1):
# 	for j in range(N-i+1):
# 		interval_sum = sum(R[j:j+i])
# 		# sums.append(interval_sum)
# 		min_sum = min(min_sum, interval_sum)
	
print(min_sum)