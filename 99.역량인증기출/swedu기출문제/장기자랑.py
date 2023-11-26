N, S, M = map(int, input().split())

people = list(range(1, N+1))
result = []

current_idx = (S - 1) % N

while people:
    current_idx = (current_idx - 1 + M) % len(people)
    result.append(people.pop(current_idx))

print(" ".join(map(str, result)))


# 입력:
# 7 1 4
# 출력:
# 4 1 6 5 7 3 2 