import sys

def input_data():
	readl = sys.stdin.readline
	n = int(readl())
	a = [list(map(int, readl().split())) for y in range(n)]
	return n, a


# 입력
# N : 장비에 장착된 노즐의 가로, 세로 개수
# A : 각 노즐의 오염도 정보
sol = -1
N, A = input_data()

# 코드를 작성하세요
def solve(A):
	even_sum = [sum(row[0::2]) for row in A]
	odd_sum = [sum(row[1::2]) for row in A]
	sum1 = sum([max(i,j) for i,j in zip(odd_sum, even_sum)])
	
	even_sum = [sum(col[0::2]) for col in zip(*A)]
	odd_sum = [sum(col[1::2]) for col in zip(*A)]
	sum2 = sum([max(i,j) for i,j in zip(odd_sum, even_sum)])
	
	return max(sum1,sum2)

sol = solve(A)
# 출력
print(sol)


#2차원 행<->열 변경방법
A_transpose = [col for col in zip(*A)]