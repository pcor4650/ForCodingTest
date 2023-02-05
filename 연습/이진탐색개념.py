import sys

input = sys.stdin.readline

n, target = map(int, input().split())
array = list(map(int, input().split()))

def bin_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            start = mid + 1
        else :
            end = mid - 1
    return None


result = bin_search(array, target, 0, n-1)

if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result+1)