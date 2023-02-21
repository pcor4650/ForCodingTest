import sys

def input_data():
	readl = sys.stdin.readline
	loop = readl().strip()
	return loop

def analysis_loop(str_loop, s):
	idx = s
	cnt = int(str_loop[s+1])
	while cnt:
		cnt -= 1
		idx = s+2
		while str_loop[idx] != '>':
			if str_loop[idx] == '<':
				idx = analysis_loop(str_loop, idx)
			else:
				print(str_loop[idx], end='')
			idx += 1
	return idx

loop = input_data()
analysis_loop(loop, 0)

# 입력:
# <3ABC>
# <2A<3B>CE>
# 출력:
# ABCABCABC
# ABBBCEABBBCE