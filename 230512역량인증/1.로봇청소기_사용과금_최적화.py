# 최적화:
# 수정전 로봇청소기 1회 사용 시작시간과 종료시간을 이용하여 요금을 계산한 코드

def InputData():
    s = input()
    e = input()
    return s, e

def ComputeTime():
    global stime
    global etime
    s = int(stime[0:2]) * 60 + int(stime[3:])
    e = int(etime[0:2]) * 60 + int(etime[3:])
    return (e - s) % 1440   #수정 : 두 시간 간 차이가 음수이더라도 %연산자 사용하면 양수 시간차로 변경해줌
    # if e-s >0:

def Solve():
    t = ComputeTime()
    if t <= 30 : p = 500
    else:
        #10분에서 1분이라도 초과하면 300 추가 과금
        if (t-30) % 10 != 0:
            p = 500 + ((t - 30) // 10 + 1) * 300
        else:
            p = 500 + ((t - 30) // 10 ) * 300
        # p값이 30000을 넘으면 30000 넣어줌
        p = min(p, 30000)
    return p

def OutputData(sol):
    print(sol)

stime, etime = InputData() #입력 
sol = Solve() # 문제 해결
OutputData(sol) # 출력



#입력 : 
# 00:00
# 00:31
#출력
# 800