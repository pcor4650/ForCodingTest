# 1.횡단보도위 위치가  백만개로 구분되고 각 위치에 사람이 있음
# 2.횡단보도위 임의위치에 광고판이 세워지는데  세워진높이만큼의 거리까지 좌우로 있는 사람들이 이 광고판을 볼수 있음
# 3.광고판을 볼수 있는 사람들의 합을 기대값 E라고 할때 기대값이상을 만족하는 광고판의 최소높이를 구하라
# 4.입력은 횡단보도위 위치값과 그위치에 서있는 사람수가 십만개까지 주어지고 기대값 E가 주어짐
# 5.출력은 광고판의 최소높이
# 6.볼수 있는 사람이 많은 위치를 찾는게 아니라  기대값을 만족하는 최소 높이를 찾음

N = 0  # 횡단보도수
E = 0  # 기대효과
Q = [0] * (100000 + 10)  # 이용자수
P = [0] * (100000 + 10)  # 횡단보도 위치
D = [0] * (1000000 + 10)  # 위치별 이용자수배열
maxP = 0  # 이용자수가 있는 최대위치


def InputData():
    global N, E, Q, P, D, maxP
    N, E = map(int, input().split())
    for i in range(N):
        Q[i], P[i] = map(int, input().split())
        D[P[i]] = Q[i]
        if P[i] > maxP:
            maxP = P[i]


# d길이 구간이 E기대효과를 충족하는지 판단
def IsEOK(d):
    global D, maxP, E
    sum = 0
    for i in range(d):
        if not D[i]:
            continue
        sum += D[i]
        if sum >= E:
            return True
    for a in range(1, maxP - d + 2):
        b = a + d - 1
        if D[a - 1]:
            sum -= D[a - 1]
        if D[b]:
            sum += D[b]
        if sum >= E:
            return True
    return False


def main():
    global N, E, Q, P, D, maxP
    ans = -1
    s, e, m = 0, maxP + 1, 0
    InputData()

    while e >= s:
        m = (s + e) // 2
        if IsEOK(m):
            e = m - 1
        else:
            s = m + 1

    ans = s // 2
    print(ans)


if __name__ == '__main__':
    main()
