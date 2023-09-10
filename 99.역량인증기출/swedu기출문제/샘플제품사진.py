import sys

input = sys.stdin.readline

N = int(input())
array = []
id_set = set()
for _ in range(N):
    pos, id = map(int, input().split())
    array.append([pos, id])
    id_set.add(id)

new_id = dict()
cnt_id = 0

for id in sorted(list(id_set)):
    new_id[id] = cnt_id
    cnt_id += 1

new_array = []
for x, i in array:
    new_array.append([x, new_id[i]])
new_array.sort()

check = [0]*cnt_id

min_length = 2000000001
s = 0

for e in range(N):
    check[new_array[e][1]] += 1
    print("s: ", s, ", e: ", e, ", check: ", check )
    while 0 not in check:
        print("min_length: ", min_length, ", new_array[e][0] - new_array[s][0]: ", new_array[e][0] - new_array[s][0])
        min_length = min(min_length, new_array[e][0] - new_array[s][0])
        check[new_array[s][1]] -= 1
        s += 1
print(min_length)