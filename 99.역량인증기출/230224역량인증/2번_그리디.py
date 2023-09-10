# 조건
# 1)N*N 격자
# 2)각 칸 숫자, 
# 3)모든 행 열의 합이 동일하도록 하면서
# 4)추가되는 제품의 수량이 최소가 되도록

# 입력
# 3
# 1 2 3
# 4 2 3
# 3 2 1

# 시험 당시 풀이: 
# row_sum = [6, 9, 6]
# col_sum = [8, 6, 7]
# 합 : 42
# col, row의 최고 숫자 : 9
# 54-42 = 12 
#  -> /2 = 6


# 답:
import sys


def InputData():
	readl = sys.stdin.readline
	N = int(readl())
	Box = [list(map(int, readl().split())) for r in range(N)]
	return N, Box


ans = -1
# 입력 함수
##N : 상자의 크기

N, Box = InputData()
# 여기서부터 작성
# for k in Box:
# 	print(k)

row_sum = []
col_sum = []
for row in Box:
	row_sum.append(sum(row))
max_row = max(row_sum)

a =  list(zip(*Box))
for col in a:
	col_sum.append(sum(col))
max_col = max(col_sum)
# print(col_sum)

max_num = max(max_row, max_col)
# print(max_num)

ans = ((2*N*max_num) - (sum(row_sum)+sum(col_sum)))//2
# 출력
print(ans)