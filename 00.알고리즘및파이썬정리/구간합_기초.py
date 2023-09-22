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

for interval in range(s, e+1):
    for start in range(1, n-interval+1):
        left = start
        right = start + interval -1
        interval_sum = prefix_sum[right] - prefix_sum[left-1]
        min_sum = min(min_sum, interval_sum)
        print("left:", left, ", right:", right, ", interval_sum:", interval_sum, ", min_sum: ", min_sum)
print(min_sum)


# For 간격 range(간격):
    # For start in range(1, n-간격+1):