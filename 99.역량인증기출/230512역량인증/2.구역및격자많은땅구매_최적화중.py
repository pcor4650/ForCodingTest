
# 제출, 수정필요사항 추가:
import sys


def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	map_area = [list(readl().strip()) for _ in range(N)]
	return N, map_area

ans = "" #구매자 이름 Buyer's name
areacnt = 0 #구매자 영역 개수 Number of buyer's area

# 입력 받는 부분 Input
N, map_area = Input_Data()

# 여기서부터 작성 Write from here

# 요렇게 딕셔너리로 만들어서 비교 연산 하고 싶었는데 포기 # owner_land = dict()  
# # owner_land = {'R:[2, 10]', 'G':[2, 5], 'B':[2,10]}
# print("owner_land", owner_land)
RGBareacnt = [0, 0, 0]		# R, G, B 구역 개수 연산을 위한 리스트
RGBsquarecnt = [0, 0, 0]	# R, G, B  격자 개수 연산을 위한 리스트

# 재귀 호출은 함수 호출 스택을 사용하므로 깊은 재귀 호출이 발생할 경우 성능에 영향을 줄 수 있다.
# def dfs(sy, sx, owner): 
# 	if sy<0 or sx<0 or sy>=N or sx>=N:
# 		return 0
# 	if map_area[sy][sx] != owner:
# 		return 0
# 	map_area[sy][sx] = 'X'
# 	return 1 + dfs(sy+1, sx, owner) + dfs(sy, sx+1, owner) + dfs(sy-1, sx, owner) + dfs(sy, sx-1, owner)

def dfs(sy, sx, owner):
	stack = [(sy, sx)]
	count = 0
	while stack:
		y, x = stack.pop()
		if y < 0 or x < 0 or y >= N or x >= N or map_area[y][x] != owner:
			continue
		map_area[y][x] = 'X'
		count += 1
		stack.append((y+1, x))
		stack.append((y, x+1))
		stack.append((y-1, x))
		stack.append((y, x-1))
	return count


# R, G, B의 구역 및 격자 개수 연산
for i in range(N):
	for j in range(N):
		if map_area[i][j] != 'X':
			owner = map_area[i][j]
			idx = 'RGB'.index(owner)
			RGBareacnt[idx] += 1
			RGBsquarecnt[idx] += dfs(i, j, owner)
# print("RGBareacnt: ", RGBareacnt)
# print("RGBsquarecnt: ", RGBsquarecnt)


# 구역의 개수 비교 -> 격자의 개수 비교 -> 격자의 개수도 같다면 -> R, G, B 순으로 구매할 땅 선택
# owner_land = {'R': [2, 10], 'G': [2, 5], 'B': [2, 10]}

# selected_color = None
# max_area_cnt = 0
# max_square_cnt = 0

# for color, (area_cnt, square_cnt) in owner_land.items():
#     if area_cnt > max_area_cnt or (area_cnt == max_area_cnt and square_cnt > max_square_cnt):
#         selected_color = color
#         max_area_cnt = area_cnt
#         max_square_cnt = square_cnt

# print(selected_color, max_area_cnt)


maxAreacnt = max(RGBareacnt)
areaIdx = []
for i in range(len(RGBareacnt)):
	if RGBareacnt[i] == maxAreacnt:
		areaIdx.append(i)
# print("areaIdx: ", areaIdx)
idx_owner = {0:"R", 1:"G", 2:"B"}


squareIdx = []
tmp_sq = 0
if len(areaIdx) == 1:
	ans = idx_owner[areaIdx[0]]
	areacnt = RGBareacnt[areaIdx[0]]
else:
	for tmp_idx in areaIdx:
		# print(tmp_idx)
		tmp_sq = max(tmp_sq, RGBareacnt[tmp_idx])
	for tmp_idx in areaIdx:
		if tmp_sq == RGBareacnt[tmp_idx]:
			squareIdx.append(tmp_idx)
	# print("squareIdx: ", squareIdx)
	if len(squareIdx) != 0:
		ans = idx_owner[squareIdx[0]]
		areacnt = RGBareacnt[squareIdx[0]]



# 출력하는 부분 Output
print(ans, areacnt)




# 입력 : 
# 5
# RRRBB
# GGBBB
# BBGRR
# BBGGR
# BRRRR

# 출력:
# R 2