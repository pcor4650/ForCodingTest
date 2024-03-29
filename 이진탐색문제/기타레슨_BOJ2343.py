# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# data = list(map(int, input().split()))

# s, e = max(data), sum(data)     # 블루레이의 최대 길이는 리스트의 합, 최소 길이는 리스트의 최댓값이다.

# while s<=e:
#     mid = (s+e) // 2
#     cnt = 0     #블루레이 개수
#     tmp = 0     #블루레이 길이
#     for i in range(n):
#         if tmp + data[i] > mid:
#             cnt += 1
#             tmp = 0       
#         tmp += data[i]
#     cnt += 1 if tmp else 0

#     if cnt <= m:
#         e = mid - 1
#     else : 
#         s = mid + 1
# print(s)

# 문제 백준 2343번
# 강토는 자신의 기타 강의 동영상을 블루레이로 만들어 판매하려고 한다. 
# 블루레이에는 총 N개의 강의가 들어가는데, 블루레이를 녹화할 때, 강의의 순서가 바뀌면 안 된다. 순서가 뒤바뀌는 경우에는 강의의 흐름이 끊겨, 학생들이 대혼란에 빠질 수 있기 때문이다. 
# 즉, i번 강의와 j번 강의를 같은 블루레이에 녹화하려면 i와 j 사이의 모든 강의도 같은 블루레이에 녹화해야 한다.
# 강토는 이 블루레이가 얼마나 팔릴지 아직 알 수 없기 때문에, 블루레이의 개수를 가급적 줄이려고 한다. 
# 오랜 고민 끝에 강토는 M개의 블루레이에 모든 기타 강의 동영상을 녹화하기로 했다. 이때, 블루레이의 크기(녹화 가능한 길이)를 최소로 하려고 한다. 단, M개의 블루레이는 모두 같은 크기이어야 한다.
# 강토의 각 강의의 길이가 분 단위(자연수)로 주어진다. 이때, 가능한 블루레이의 크기 중 최소를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 강의의 수 N (1 ≤ N ≤ 100,000)과 M (1 ≤ M ≤ N)이 주어진다.                                            9 3
# 다음 줄에는 강토의 기타 강의의 길이가 강의 순서대로 분 단위로(자연수)로 주어진다. 각 강의의 길이는 10,000분을 넘지 않는다.        1 2 3 4 5 6 7 8 9

# 출력
# 첫째 줄에 가능한 블루레이 크기중 최소를 출력한다.                                                                  17


# 1 2 3 4 5 | 6 7 | 8 9


# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())
# datas = list(map(int, input().split()))

# s = max(datas)
# e = sum(datas)

# def bin_search(start, end, datas):
#     while start <= end:
#         print("start: ", start, " end: ", end)
#         mid = (start+end) // 2
#         cnt = 0
#         tmp_length = 0
#         b = []

#         for data in datas:
#             print("mid: ",mid, ", data: ", data, ", tmp_length: ", tmp_length)
#             if tmp_length + data > mid:
#                 cnt += 1
#                 tmp_length = 0
#             tmp_length += data
#         if tmp_length != 0:
#             cnt += 1

#         print("cnt: ", cnt)
#         if cnt < M:
#             end = mid - 1
#         elif cnt == M:
#             end = mid -1
#             b.append(mid)
#         else:
#             start = mid + 1
#     return start, end, b

# start, end, b = bin_search(s, e, datas)
# print(b)

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
lec_length = list(map(int, input().split()))

start = max(lec_length)
end = sum(lec_length)

def bin_search(array, s, e):
    while s <= e:
        mid = (s+e) // 2
        tmp_length = 0
        cnt = 0

        for a in array:
            if tmp_length + a > mid:
                cnt += 1
                tmp_length = 0
            tmp_length += a
        if tmp_length != 0:
            cnt += 1

        
        
        if cnt <= M:
            e = mid - 1
        else: 
            s = mid + 1
    return s, e

s, e = bin_search(lec_length, start, end)

print(s)
