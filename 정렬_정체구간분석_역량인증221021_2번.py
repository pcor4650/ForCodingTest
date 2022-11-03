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