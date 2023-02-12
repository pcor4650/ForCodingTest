import sys
input = sys.stdin.readline

N, M = map(int, input().split())
Trees = list(map(int, input().split()))

start = 0
end = max(Trees)

maxH = 0
while start <= end:
    mid = (start + end) // 2
    tmp_length = 0
    
    for tree in Trees:
        if tree > mid:
            tmp_length += (tree-mid)
    
    if tmp_length < M:
        end = mid - 1
    else:
        start = mid + 1
        maxH = max(maxH, mid)

print(maxH)