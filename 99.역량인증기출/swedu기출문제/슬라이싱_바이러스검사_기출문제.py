import sys

def InputData():
    readl = sys.stdin.readline
    N, M = map(int, readl().split())
    Data = list(map(int, readl().split()))
    Virus = list(map(int, readl().split()))
    return N, M, Data, Virus

# 기초 바이러스로 변환
global Virus
Virus.sort()
Virus = list(map(lambda x:X-[Virus[0], Virus])) 

def find(start):
    global Virus

    check_array = A[start:start+M]
    check_array.sort()
    check_array = list(map(lambda x:x-check_array[0], check_array))

    return Virus == check_array

def Solve():
    sol = 0
    for i in range(N-M+1):
        sol += find(i)
    return sol

sol = 0
N, M, Data, Virus = InputData()
sol = Solve()
print(sol)