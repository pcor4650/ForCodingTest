import sys
 
def input_data():
    readl = sys.stdin.readline
    N = int(readl())
 
    X = [0] * (N + 10)
    Y = [0] * (N + 10)
    R = [0] * (N + 10)
 
    for i in range(N) :
        X[i], Y[i], R[i] = map(int, readl().split())
    M, Q, L = map(int, readl().split())
 
    return N, X, Y, R, M, Q, L
 
sol = -1
 
# 입력
# N: 농장의 수 the number of farms
# X: 농장의 가로 위치 horizontal location of the farm
# Y: 농장의 세로 위치 vertical position of the farm
# R: 농장의 필요 강우량 Required rainfall on the farm
# M: 인공 강우 횟수 number of artificial precipitation
# Q: 인공 강우량 artificial rainfall
# L: 인공 강우 거리 artificial rain distance
 
N, X, Y, R, M, Q, L = input_data()
 
# 코드를 작성하세요 Write the code
ranis_sum = [0]*N
maxFarms = 0

def countFarms(rains_sum):
    cnt = 0
    if i in range(N):
        if rain_sum[i] >= R[i]:
            cnt += 1
    return cnt

def artificialRain(farm, rain_sum, rainCnt):
    global maxFarms
    for i in range(N):
        xDiff = abs(X[i]-X[farm])
        yDiff = abs(Y[i]-Y[farm])
        if xDiff+yDiff <= L:
            rain_sum[i] += Q
    rainCnt += 1

    if rainCnt >= M:
        farmCount = countFarms(rain_sum)
        if farmCount > maxFarms:
            maxFarms = farmCount
            return
    for i in range(N):
        artificialRain(i, rain_sum.copy(), rainCnt)

for i in range(N):
    artificialRain(i, rain_sum.copy(), 0)


# 출력 Output
print(maxFarms)

# 조합으로도 풀릴 것 같은데 해보자~