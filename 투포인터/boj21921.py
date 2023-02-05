import sys

input = sys.stdin.readline

N, X = map(int, input().split())
data = list(map(int, input().split()))

window_size = X

def sliding_window_maxsum(array, length):
    maxsum = 0
    arr_sum = []
    interval_sum = sum(array[0:length])
    arr_sum.append(interval_sum)
    maxsum = max(maxsum, interval_sum)
    for i in range(1, len(array) - length + 1):
        interval_sum = interval_sum - array[i-1] + array[i+length-1]
        arr_sum.append(interval_sum)
        maxsum = max(interval_sum, maxsum)        
    return maxsum, arr_sum

sol, arr_sum = sliding_window_maxsum(data, window_size)

if sol != 0:
    print(sol)
    print(arr_sum.count(sol))
else:
    print("SAD")    


# 입력 :
# 5 2           N, X   , 블로그 작성 5일차, 2일간 최대 방문자 수는?
# 1 4 2 5 1     data   방문자 수

# 출력 :
# 7
# 1