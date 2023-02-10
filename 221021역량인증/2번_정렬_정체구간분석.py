import sys
 
def InputData():
    readl = sys.stdin.readline
    N, T = map(int, readl().split())
    arr = [  readl().split() for i in range(N) ]
    G = [ int(x[0]) for x in arr ]
    S = [ int(x[1]) for x in arr ]
    return N, T, G, S
  
N, T, G, S = InputData() # 차량수, 측정시간, 차량 구간번호, 차량 속도
 
# 코드를 작성하세요
carList = []
for i in range(N):
    carList.append([G[i],S[i]])
carList.sort(key=lambda x:x[0])     #초기 위치 기준으로 정력

for i in reversed(range(N)):
    if i == N-1:
        carList[i][0] = carList[i][0] + T*carList[i][1]
        if carList[i][0] > int(1e9)
            carList[i][0] = int(1e9)
    else:
        carList[i][0] = min(carList[i+1][0], carList[i][0] + T*carList[i][1])

final_G = [x[0] for x in carList]

maxCount = 0
for i in set(final_G):
    count = final_G.count(i)
    maxCount = max(count, maxCount)

print(maxCount)

# Description
# 놀이동산 진입로, 1차선 도로, 앞차 추월 불가능
# 정체구간 그룹 형성되는데, 여러 그룹 중 전체 차량의 수가 가장 많은 그룹의 차량 수를 구하는 문제
# 각 구간은 1km 로 구분됨, 초기에는 구간별 1대만 존재.

# N	1 <= N <= 100,000	차량수
# T	1 <= T <= 1,000,000,000	측정시간 (분)
# G	0 <= G <= 1,000,000,000	구간번호 (Km)
# S	0 <= S <= 1,000,000,000	차량속도 (Km/분)

# 입력 : 
# 5 3     // 차량 5대, 측정시간 3분
# 0 1     // 1번째 차량 구간번호 0, 구간속도 1
# 2 3
# 3 2
# 5 2
# 6 1

# 출력 :
# 4