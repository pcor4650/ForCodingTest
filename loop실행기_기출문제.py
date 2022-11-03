import sys


def input_data():
	readl = sys.stdin.readline
	loop = readl().strip()
	return loop

def analysis_loop(str_loop, s):
	p = s
	cnt = int(str_loop[s+1])
	while cnt:
		cnt -= 1
		p = s+2
		while str_loop[p] != '>':
			if str_loop[p] == '<':
				p = analysis_loop(str_loop, p)		#왜 p에 넣을까?
			else:
				print(str_loop[p], end='')
			p += 1
	return p

# 입력 받는 부분
loop = input_data()

# 코드를 작성하세요
analysis_loop(loop, 0)
