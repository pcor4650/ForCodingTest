# 특정한 합을 가지는 부분 연속 수열 찾기

n = 5   # 데이터의 개수
m = 5   # 찾고자 하는 부분합 M
data = [1, 2, 3, 2, 5]  # 전체 수열

count = 0
interval_sum = 0
end = 0

#start를 차례대로 증가시키며 반복
for start in range(n):
    # end를 가능한 만큼 이동시키기
    while interval_sum < m  and end < n:
        interval_sum += data[end]
        end += 1
    # 부분합이 m일 때 카운트 증가
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]

print(count)

# 알고리즘
# 1. 시작점(start)과 끝점(end)이 첫 번째 원소의 인덱스(0)dmf rkflzlehfhr gksek.
# 2. 현재 부분합이 M과 같다면 카운트한다.
# 3. 현재 부분합이 M보다 작으면 end를 1 증가시킨다.
# 4. 현재 부분합이 M보다 크거나 같으면 start를 1 증가시킨다.
# 5. 모든 경우를 확인할 때까지 2번부터 4번 까지의 과정을 반복한다.


# 정렬되어 있는 두 리스트의 합집합
n, m = 3, 4
a = [1, 3, 5]
b = [2, 4, 6, 8]

# 리스트 A와 B의 모든 원소를 담을 수 있는 크기의 결과 리스트 초기화
result = [0] * (n+m)
i = 0
j = 0
k = 0

# 모든 원소가 결과 리스트에 담길 때까지 반복
while i < n or j < m:
    # 리스트 B의 모든 원소가 처리되었거나, 리스트 A의 원소가 더 작을 때
    if j >= m or (i < n and a[i] <= b[j]):
        # 리스트 A의 원소를 결과 리스트로 옮기기
        result[k] = a[i]
        i += 1
    # 리스트 A의 모든 원소가 처리되었거나, 리스트 B의 원소가 더 작을 때
    else:
        # 리스트 B의 원소를 결과 리스트로 옮기기
        result[k] = b[j]
        j+= 1
    k += 1
# 결과 리스트 출력
for i in result:
    print(i, end=' ')

# 알고리즘
# 1. 정렬된 리스트 A와 B를 입력받는다
# 2. 리스트 A에서 처리되지 않은 원소 중 가장 작은 원소를 i가 가리키도록 한다.
# 3. 리스트 B에서 처리되지 않은 원소 중 가장 작은 원소를 j가 가리키도록 한다.
# 4. A[i]와 B[j] 중에서 더 작은 원소를 결과 리스트에 담는다.
# 5. 리스트 A와 B에서 더 이상 처리할 원소가 없을 때까지 2~4번의 과정을 반복한다.



# 구간 합 빠르게 계산하는 알고리즘
n = 5
data = [10, 20, 30, 40, 50]

# Prefix Sum 배열 계산
sum_value = 0
prefix_sum = [0]
for i in data:
    sum_value += i
    prefix_sum.append(sum_value)

# 구간 합 계산(세번째 수부터 네번째 수까지)
left = 3
right = 4
print(prefix_sum[right] - prefix_sum[left - 1])

# 1. N개의 수에 대하여 접두사 합(Prefix Sum)을 계산하여 배열 P에 저장한다.
# 2. 매 M개의 쿼리 정보 [L, R]을 확인할 때, 구간합은 P[R] - P[L-1]이다

# 예를 들어 다음과 같이 5개의 데이터가 있다고 할 때,
# 10 20 30 40 50
# 이 5개의 데이터에 대해서 접두사 합을 계산하면 다음과 같다
# 0 10 30 60 100 150
