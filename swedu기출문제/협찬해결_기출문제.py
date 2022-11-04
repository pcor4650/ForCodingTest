import sys

def input_data() :
	readl = sys.stdin.readline
	N = int(readl())#협찬 물품의 수
	D = list(map(int, readl().split()))#선호도 
	return N, D

def Solve() :
    sol = -30001
    sum = 0
    for i in D:
        if sum > 0 :
            sum += i
        else:
            sum = i
        if sum > sol:
            sol = sum