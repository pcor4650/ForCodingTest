

# 수정해보자: 
import sys
from itertools import permutations, combinations
from collections import deque
import copy

def Input_Data():
	readl = sys.stdin.readline
	R, C = map(int,readl().split())
	map_city = [readl().strip() for _ in range(R)]
	return R, C, map_city

sol = -1
# 입력 받는 부분
R, C, map_city = Input_Data()

pos = dict()
dir = [[1,0],[-1,0],[0,1],[0,-1]]
# 여기서부터 작성
# S 및 숫자 위치 저장
for i in range(R):
	for j in range(C):
		if map_city[i][j] == 'S':
			pos['S'] = [i, j]
		if map_city[i][j] != '.' and map_city[i][j] != '*':
			pos[map_city[i][j]] = [i, j]
# print(pos)

set_pos = set(list(pos))
list_pos = list(pos)

# 두 점의 위치 최단거리 BFS 구현
# S:[sy, sx], E = [ey, ex]
def bfs(S, E):
	sy, sx = S[0], S[1]
	ey, ex = E[0], E[1]
	dist = [[1000]*C for _ in range(R)]	#다른데 가야할듯
	dist[sy][sx] = 0
	Q = deque()
	Q.append([sy, sx])
	while Q:
		# print("===")
		# for k in dist:
		# 	print(k)
		y, x = Q.popleft()
		for dy, dx in dir:
			ny, nx = y+dy, x+dx
			if 0<=ny<R and 0<=nx<C and map_city[ny][nx] != '*' and dist[ny][nx] > dist[y][x]+1:
				dist[ny][nx] = dist[y][x]+1
				Q.append([ny,nx])
	return dist[ey][ex]			
# test_bfs = bfs([0,1], [3,0])

# print(P)
# print(list_pos)
# print(perm_pos_list)
# list_pos.remove('S')

comb_two = set(list(combinations(list_pos, 2)))
dist_comb_two = dict.fromkeys(comb_two, 0)
# print(dist_comb_two)
# print(comb_two)

# 두 포인트 간 최단거리 미리 구해놓기
for comb in comb_two:
	pos1, pos2 = comb
	start = pos[pos1]
	end = pos[pos2]
	dis = bfs(start, end)
	dist_comb_two[comb] = dis							# combination 반환값은 튜플로 set으로 바꿨어야
	
# for pos1 in list_pos:
# 	dist = [[1000]*C for _ in range(R)]
# 	for pos2 in list_pos:
# 		if pos1 != pos2:
# 			start = pos[pos1]
# 			end = pos[pos2]
# 			dis = bfs(start, end)
# 			dist_comb_two[(pos1, pos2)] = dis
# print(dist_comb_two)
	# print(dis)
	# print("S: ", S, "E: ", E)
# print("list_pos: ", list_pos)
# print("set_pos: ", set_pos)

perm_pos_list = copy.deepcopy(list_pos)
perm_pos_list.remove('S')
P = list(permutations(perm_pos_list,len(perm_pos_list)))

min_dis = 1000
# print(P)
for p in P:
	tmp_dis = 0
	s = pos['S']
	for g in p:
		e = pos[g]
		tmp_dis += bfs(s, e)             # 실수! : 두 포인트 간 최단 거리 미리 구해놓고 다시 BFS 실행했네, 여기만 수정해주면 될듯
		if tmp_dis > min_dis:
			break
		s = pos[g]
	e = pos['S']
	tmp_dis += bfs(s, e)                # 실수! : 두 포인트 간 최단 거리 미리 구해놓고 다시 BFS 실행했네, 여기만 수정해주면 될듯
	min_dis = min(min_dis, tmp_dis)
print(min_dis)		

# 출력하는 부분
# print(sol)

# 입력 기억 안남 아래는 기억 의존:
5 5
# .S*.1
# ..*2.
# 3....
# .....
# ...4.

# 출력(위 입력에 맞는 답 아님):
# 18 


# 위 제출 답안 수정:
