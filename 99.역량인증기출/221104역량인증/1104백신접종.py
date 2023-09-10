import sys

input = sys.stdin.readline

N, K, M = map(int, input().split())
CRT = list(map(int, input().split()))   # 고객 예약 시간
CRT.sort()

s = 0                   # N회차로 진행할 경우
e = CRT[-1] - CRT[0]    # 1회차로 진행할 경우

while s<=e:
    mid = (s+e)//2
    tmp = []
    operation = []
    # mid 값에 따라 operation 배열 만들기
    for crt in CRT:
        if len(tmp) == M:           # 아래 조건에 의해 tmp가 꽉 찼다면 operation 배열에 넣어주고, tmp 초기화
            operation.append(tmp)
            tmp = []
        if len(tmp) == 0:            # tmp 가 비어 있으면 for문 통해 들어오는 t append
            tmp.append(crt)
        elif tmp:                    # tmp가 있으면
            if crt - tmp[0] <= mid:     # 새로 들어오는 것에서 처음 시간 빼준게 mid 보다 작을 경우에만 tmp에 append
                tmp.append(crt)
            else:
                operation.append(tmp)
                tmp = []
                tmp.append(crt)
    if tmp:
        operation.append(tmp)
    # operation 배열이 만들어 졌으면 아래 조건에 따라 s, e 변경
    print("s: ",s,  ", e: ", e, "mid: ", mid)
    for k in operation:
        print(k)
    if len(operation) <= K:
        e = mid - 1
        ans = mid
        cnt = len(operation)
    else:
        s = mid + 1
print(mid, cnt)

# 문제 : http://collab.lge.com/main/pages/viewpage.action?pageId=1856030495