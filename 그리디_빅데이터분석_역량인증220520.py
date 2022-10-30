import sys
def Input_Data():
    readl = sys.stdin.readline
    N = int(input())
    l = [list(map(int, readl().split())) for n in range(N)] 
    X, Y = [list(x) for x in zip(*l)]
    return N, X, Y
sol = -1
# 입력
# N : 그룹의 수
# X : 고객의 최소 요구치
# Y : 고객의 최대 요구치
N, X, Y = Input_Data()

#코드를 작성하세요
def getOverlapped(x1, y1, x2, y2):
    newMin = max(x1, x2)
    newMax = min(y1, y2)
    return newMin, newMax

def compact(groups):
    idx = 0
    while idx < len(groups) - 1:
        newX, newY = getOverlapped(groups[idx][0], groups[idx][1], groups[idx+1][0], groups[idx+1][1])
        
        if newX <= newY:
            groups.pop(idx)
            groups.pop(idx)
            groups.insert(idx, [newX, newY])
        else:
            idx += 1
    return groups

groups = [[X[i],Y[i]] for i in range(N)]

sorted_groups = groups.sort(key=lambda x:x[0])
            

#출력
print(len(compact(sorted_groups)))