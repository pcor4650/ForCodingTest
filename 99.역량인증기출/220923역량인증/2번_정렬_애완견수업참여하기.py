#2. 정답, 백준 1931과 유사

import sys


def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	info = [list(map(int,readl().split())) for _ in range(N)]
	return N, info

ans = 1
N, info = Input_Data() # 입력 받는 부분

# 여기서 부터 작성
# for i in range(N):
# 	info[i][1] = info[i][0] + info[i][1] + 2

info.sort(key = lambda x:x[0])
info.sort(key = lambda x:x[1])

end = info[0][1]

for j in range(1,N):
	if info[j][0] >= end:
		ans += 1
		end = info[j][1]
		

print(ans) # 출력 하는 부분