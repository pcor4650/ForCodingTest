#한 번 계산된 결과를 메모이제이션 하기 위한 리스트 초기화
d = [0]*100

#피보나치 함수를 재귀함수로 구현
def fibo(x):
    #종료 조건
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    dx = fibo[x-1] + fibo[x-2]
    return d[x]