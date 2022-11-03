import sys
  
def InputData():
    readl = sys.stdin.readline
    N = int(readl())
    A = [list(map(int,readl().split())) for _ in range(N)]
    return N, A
  
  
def Solve():
    maxint = 0
    A.sort(key = lambda x: x[0])
    start = A[0][0]
    maxint= A[0][1] - start
     
    for i in range(1, N):
        if A[i-1][1] >= A[i][0]:
            if maxint < A[i][1] - start:
                maxint = A[i][1] - start
        else:
            start = A[i][0]
            maxint = max(maxint, A[i][1]-start)
         
    return maxint
  
ans = -1
N, A = InputData()
ans = Solve()
print(ans)