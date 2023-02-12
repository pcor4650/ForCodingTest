# import sys
# input = sys.stdin.readline

# N = int(input())
# A = list(map(int, input().split()))
# N = int(input())
# test_data = list(map(int, input().split()))

# ################################################################
# A.sort()

# for data in test_data:
#     start, end = 0, N-1
#     check = 0
#     while start <= end:
#         mid = (start+end)//2
#         # print("start = ", start, ", end = ", end, ", mid = ", mid, ", data = ", data, ", A[mid] = ", A[mid])
#         if A[mid] <= data:
#             start = mid + 1
#             if A[mid] == data:
#                 check = 1
#         elif A[mid] > data:
#             end = mid - 1

#     print(check)

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
test_data = list(map(int, input().split()))

A.sort()

for data in test_data:
    start, end = 0, len(A)-1
    check = 0
    while start <= end:
        mid = (start+end)//2
        if A[mid] < data:
            start = mid + 1   
        elif A[mid] > data:
            end = mid - 1
        elif A[mid] == data:
            check = 1
            break

    print(check)