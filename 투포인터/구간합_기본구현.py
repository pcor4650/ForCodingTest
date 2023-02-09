#구간 합 빠르게 계산하기 알고리즘
 #1. N개의 수에 대하여 Prefix Sum을 계산하여 배열 P에 저장한다
 #2. 매 M개의 쿼리 정보 [L, R]을 확인할 때, 구간합은 P[R] - P[L-1] 이다.
 
# n = 5
# data = [10, 20, 30, 40, 50]

# # Prefix Sum 배열 계산
# sum_value = 0
# prefix_sum = [0]
# for i in data:
#     sum_value += i
#     prefix_sum.append(sum_value)
    
# print(prefix_sum)

# # 구간 합 계산, 세번째에서 네번째까지의 합을 구하고 싶으면
# left = 3
# right = 4
# result = prefix_sum[right] - prefix_sum[left-1]
# print(result)

# s, e 가 있을 때? 인터벌의 합이 가장 작은 것은
# 230203 역량인증 2번 아래와 같이 풀면 맞을 듯
n, s, e = 5, 1, 2
datas = [3, -1, -2, 3, 1]

min_sum = 10000000
prefix_sum = [0]
summ_value = 0
for dta in datas:
    summ_value += dta
    prefix_sum.append(summ_value)

print("prefix_sum: ", prefix_sum)

for i in range(s, e+1):
    for j in range(1, n-i+1):
        left = j
        right = j + i -1
        part_sum = prefix_sum[right] - prefix_sum[left-1]
        min_sum = min(min_sum, part_sum)
        print("left:", left, ", right:", right, ", part_sum:", part_sum, ", min_sum: ", min_sum)
print(min_sum)