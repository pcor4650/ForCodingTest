import sys
 
def Input_Data():
    readl = sys.stdin.readline
    T = int(readl())
    Data = [int(readl()) for i in range(T)]
    return T, Data
 
# 입력
# T : 입력 데이터의 개수, 1 ~ 1000
# Data : 통나무의 개수, 1 ~ 20,000
# sol : 필요한 창고의 개수
T, Data = Input_Data()
sol = [0] * T
 
logNums = [0] * 20001
# 코드를 작성하세요
storageIsOne = []
for i in range(1,200):
    if i * (i+1) / 2 < 20000:        
        storageIsOne.append(int(i * (i+1) / 2))
        logNums[int(i*(i+1)/2)] = 1
                
storageIsTwo = []        
for i in storageIsOne:
    for j in storageIsOne:
        if i + j <= 20000 and logNums[i+j] == 0:
            storageIsTwo.append(i+j)
            logNums[i+j] = 2           

storageIsThree = []
for i in storageIsOne:
    for j in storageIsOne:
        for k in storageIsOne:
            if i+j+k<=20000 and logNums[i+j+k] == 0:
                storageIsThree.append(i+j+k)
                logNums[i+j+k] = 3                 
    
##logNums[1~20000] 모두 할당 됨
count = 0
for i in range(1,20001):
    if logNums[i] == 0:
        count+=1
# print(count)  0출력됨
                    
for i in range(0, len(Data)):        
    sol[i] = logNums[Data[i]]
 
print(*sol, sep='\n')




# tip!
# i*(i+1)/2 번째 인덱스는 모두 1이 되어야 한다. 1, 3, 6, 10, 15, 21, 28, ..., 19900
