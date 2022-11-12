# given code
import sys
 
def input_data():
    readl = sys.stdin.readline
    x = [0] * 100000
    y = [0] * 100000
    n = int(readl())
    data = []
    for i in range(n):
        x[i], y[i] = map(int, readl().split())
        data.append([x[i], y[i]])
 
    return n, data
 
# 입력
# N : 기념품점의 개수
# X : 출발점으로부터의 거리
# Y : 머그컵의 가격



sol = -1
N, data= input_data()
data.sort()
 
# 코드를 작성하세요
INF = 987654321
buy_result = [INF]*N
buy_result[N-1] = data[N-1][1]
for i in reversed(range(N-1)):
    if data[i][1] < buy_result[i+1]:
        buy_result[i] = data[i][1]
    elif data[i][1] > buy_result[i+1]:
        buy_result[i] = buy_result[i+1]

sol = sum(buy_result)
# 출력
print(sol)




# Description
# 기념품가게에서 머그컵을 사야 하는데 거리가 가까운 상점부터 한 군데 씩 상점에 들린다.
# 현재 들른 가게보다 더 싸게 파는 가게가 뒤에 없으면 현재 가게에서 머그컵을 사고, 만약 현재 가게보다 조금이라도 더 싸게 파는 가게가 있다면 현재 가게보다 싼 가장 가까운 가게에서 산다.
# 모든 머그컵을 사는데 들어가는 총 비용은?

# N	1<=N<=100,000	상점의 수
# X	0<=X<=1,000,000,000	상점가지의 거리
# Y	1<=Y<=1,000,000	머그컵의 가격

# 입력 : 
# 4
# 2 40
# 10 12
# 5 7
# 9 15

# 출력 : 
# 38

# 5             61
# 1 15
# 2 14
# 3 13
# 4 12
# 5 11

# 풀이
# 1. 거리 기준으로 정렬
# 거리 :      2   5   9   10
# 기념품가격 :  40  7  15   12
# buy_result 7   7   12  12 

# 2.buy확정 배열 만들어 뒤에 부터 채워나감
# buy = [INF]*N
# buy확정 : buy[N-1] = 제일 먼 거리의 기념품 가격 12