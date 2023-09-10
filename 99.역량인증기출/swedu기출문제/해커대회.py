
# 일부 타임 아웃, 백준 1406 문제와 비슷
S = list(input().strip())
C = input().strip()

idx = len(S)

for c in C:
	if c=="L" and idx>0:
		idx -= 1
	elif c=="R" and idx < len(S):
		idx += 1
	elif c=="B" and idx > 0:
		S.pop(idx-1)
		idx -= 1
	else:
		if ord('a') <= ord(c) <= ord('z'):
			S.insert(idx, c)
			idx += 1
			
print("".join(S))