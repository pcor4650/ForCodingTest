0826 SW 역량 테스트 2번 문제 답

from collections import deque

#input data 시작시간과 길이를 S와 T배열에 받기 K값 받기 등

#생략

# k 개의 큐 만들기
q = [deque() for _ in range(K)]

result = [0 for _ in range(K)]

for st, t in zip(S, T):
	cur = st
	for i in range(K):
		while q[i]:
			if q[i][0] < cur:
				q[i].popleft()
				result[i] += 1
				continue
			break
	
	min_que_idx = 0
	min_que_size = int(1e9)
	for i in range(K):
		if not q[i]:
			min_que_idx = i
			break
		if len(q[i]) < min_que_size:
			min_que_size = len(q[i])
			min_que_idx = i
			
	if not q[min_que_idx]:
		q[min_que_idx].append(st+t-1)
	else:
		q[min_que_idx].append(q[min_que_idx][-1] + t)

sol = 0

for i in range(K):
	result[i] += len(q[i])
	sol = max(sol, q[i][-1])
	
print(sol)
print(*reset)
