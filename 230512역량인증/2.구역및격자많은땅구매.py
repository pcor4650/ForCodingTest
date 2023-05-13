# N*N에 R, G, B가 있음
# 1. DFS로 R, G, B 구역의 개수 구하기
#  방문여부 배열 필요
# 2. N*N 돌며 R, G, B의 각 개수 구하기


# 딕셔너리 

# R,G,B중 구역이 가장 많은 소유자의 땅 구매
# 구역이 동일하면 격자의 개수가 가장 많은 소유자의 땅 구매
# 격자의 개수가 동일하면 R,G,B 순 선택

# 입력 : 
# 5
# RRRBB
# GGBBB
# BBGRR
# BBGGR
# BRRRR

# 출력:
# R 2


# 제출, 수정필요사항 추가:
import sys
from collections import deque


def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	map_area = [list(readl().strip()) for _ in range(N)]
	return N, map_area

#구매자 이름 Buyer's name
ans = ""
#구매자 영역 개수 Number of buyer's area
areacnt = 0

# 입력 받는 부분 Input
N, map_area = Input_Data()

# 여기서부터 작성 Write from here
dir = [[1,0],[-1,0],[0,1],[0,-1]]

# 아래에서 두개 뒤바꿔서 사용함
RGBareacnt = [0, 0, 0]		# R, G, B 구역 개수 연산을 위한 리스트
RGBsquarecnt = [0, 0, 0]	# R, G, B  격자 개수 연산을 위한 리스트
# RGBareacnt[0] = RGBareacnt[0] + 1
# print("RGBareacnt: ", RGBareacnt)

# visit 배열 안쓰려면?
visited = [[0]*N for _ in range(N)]
# print("visited: ",visited)

#최적화 필요 : 
# 1. dfs를 bfs처럼 코드 작성, 최적화 필요
# 2. "R", "G", "B" 인자 받을 수 있게 파라미터 하나 더 추가 필요
def dfs(sy, sx): 
	if visited[sy][sx] != 0:
		return 0
	visited[sy][sx] = 1
	q = deque()
	q.append([sy, sx])
	while q:
		y, x = q.popleft()
		visited[y][x] = 1
		for dy, dx in dir:
			ny, nx = y+dy, x+dx
			if 0<=ny<N and 0<=nx<N and map_area[ny][nx] == map_area[sy][sx] and visited[ny][nx]==0:
				visited[ny][nx] = 1
				q.append([ny,nx])
	return 1

# R, G, B의 구역 및 격자 개수 연산
for i in range(N):
	for j in range(N):
		if map_area[i][j] == 'R':
			RGBareacnt[0] += 1
			# if visited[i][j] == 0:
			RGBsquarecnt[0] += dfs(i, j)
		elif map_area[i][j] == 'G':
			RGBareacnt[1] += 1	
			# if visited[i][j] == 0:
			RGBsquarecnt[1] += dfs(i, j)
		elif map_area[i][j] == 'B':
			RGBareacnt[2] += 1
			# if visited[i][j] == 0:
			RGBsquarecnt[2] += dfs(i, j)

# print("RGBareacnt: ", RGBareacnt)
# print("RGBsquarecnt: ", RGBsquarecnt)

# 구역의 개수 비교 -> 격자의 개수 비교 -> 격자의 개수도 같다면 -> R, G, B 순으로 구매할 땅 선택

# 요렇게 딕셔너리로 만들어서 비교 연산 하고 싶었는데 포기 # owner_land = dict()  
# # owner_land = {'R:[2, 10]', 'G':[2, 5], 'B':[2,10]}
# print("owner_land", owner_land)
maxSquarecnt = max(RGBsquarecnt)
square_idx = []
for i in range(len(RGBsquarecnt)):
	if RGBsquarecnt[i] == maxSquarecnt:
		square_idx.append(i)
# print("square_idx: ", square_idx)
idx_owner = {0:"R", 1:"G", 2:"B"}


area_idx = []
tmp_sq = 0
if len(square_idx) == 1:
	ans = idx_owner[square_idx[0]]
	areacnt = RGBsquarecnt[square_idx[0]]
else:
	for tmp_idx in square_idx:
		# print(tmp_idx)
		tmp_sq = max(tmp_sq, RGBareacnt[tmp_idx])
	for tmp_idx in square_idx:
		if tmp_sq == RGBareacnt[tmp_idx]:
			area_idx.append(tmp_idx)
	# print("area_idx: ", area_idx)
	if len(area_idx) != 0:
		ans = idx_owner[area_idx[0]]
		areacnt = RGBsquarecnt[area_idx[0]]



# 출력하는 부분 Output
print(ans, areacnt)




# 시간 초과 원인 검사를 위한 TC 생성
# 80
# RRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# RRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# GGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# BBGRRRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# BBGGRRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# BRRRRRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# RRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# RRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# RRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# RRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# GGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# BBGRRRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# BBGGRRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# BRRRRRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# RRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# RRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# RRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# RRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# GGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# BBGRRRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# BBGGRRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# BRRRRRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# RRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# RRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# RRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# RRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# GGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# BBGRRRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# BBGGRRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# BRRRRRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# RRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# RRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# RRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# RRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# GGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# BBGRRRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# BBGGRRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# BRRRRRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# RRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# RRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# RRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# RRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# GGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# BBGRRRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# BBGGRRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# BRRRRRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# RRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# RRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# RRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# RRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# GGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# BBGRRRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# BBGGRRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# BRRRRRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# RRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# RRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# RRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# RRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# GGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# BBGRRRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# BBGGRRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# BRRRRRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# RRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# RRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# RRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# RRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# GGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# BBGRRRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# BBGGRRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# BRRRRRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# RRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# RRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# RRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# RRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# GGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# BBGRRRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# BBGGRRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# BRRRRRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# RRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB
# RRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBGGBBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBBRRRBB