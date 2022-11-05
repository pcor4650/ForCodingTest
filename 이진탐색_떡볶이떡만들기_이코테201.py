n, m = map(int, input().split())
H = list(map(int, input().split()))

H.sort()
s = 0
e = max(H)

while s <= e:
    total = 0
    mid = (s+e) // 2
    for x in H:
        if x > mid:
            total += x - mid
    # 떡의 양이 부족하다면
    if total < m:
        end = mid -1
    else :
        start = mid + 1
        result = mid
        
print(result)


# 입력 조건 :
# 첫째 줄에 떡의 개수 N(1~1,000,000)과 요청한 떡의 길이 M(1~2,000,000,000)이 주어진다       4 6
# 둘째 줄에는 떡의 개별 높이가 주어진다. 떡 높이의 총합은 항상 M 이상으로 0~1,000,000,000       19 15 10 17   -> 정렬 필요  10 15 17 19

# 출력 조건:
# 적어도 M만큼의 떡을 집에 가져가기 위해 절단기에 설정할 수 있는 높이의 최대값 출력                15