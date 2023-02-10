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


# s, e 가 있을 때? 인터벌의 합이 가장 작은 것은
# 230203 역량인증 2번 아래와 같이 풀면 맞을 듯
n, s, e = 5, 1, 2
datas = [3, -1, -2, 3, 1]

min_sum = 10000000
prefix_sum = [0]
summ_value = 0
for dta in datas:
    summ_value += dta
    prefix_sum.append(summ_value)

print("prefix_sum: ", prefix_sum)

for i in range(s, e+1):
    for j in range(1, n-i+1):
        left = j
        right = j + i -1
        part_sum = prefix_sum[right] - prefix_sum[left-1]
        min_sum = min(min_sum, part_sum)
        print("left:", left, ", right:", right, ", part_sum:", part_sum, ", min_sum: ", min_sum)
print(min_sum)