import sys
readl = sys.stdin.readline

n = int(input())
storeParts = list(map(int, input().split()))
m = int(input())
askParts = list(map(int, input().split()))

storeParts.sort()

def binary_search(array, targetPart, s, e):
    while s <= e:
        mid = (s+e) // 2
        if array[mid] == targetPart:
            return True
        elif array[mid] > targetPart:
            e = mid - 1
        else :
            s = mid + 1
    return False

isPartExist = []
for part in askParts:
    if binary_search(storeParts, part, 0, n-1):
        isPartExist.append("yes")
    else:
        isPartExist.append("no")

print(*isPartExist, sep=" ")


# 입력 조건 : 
# 첫째 줄에 정수 N (1~1,000,000), 가게이 있는 부품 수                                  5
# 둘째 줄에 공백 구분하여 N개의 정수가 주어진다. 이때 정수는 1~1,000,000 사이의 정수이다        8 3 7 9 2   -> 정렬 필요
# 셋째 줄에 정수 M이 주어진다(1~100,000), 손님의 확인 요청한 부품 수                       3
# 넷째 줄에는 공백으로 구분하여 M개의 정수가 주어진다. 이때 정수는 1~1,000,000 사이            5 7 9

# 출력 조건 :
# 첫째 줄에 공백으로 구분하여 각 부품이 존재하면 yes를, 없으면 no를 출력한다                   no yes yes


# 접근 방법
# 1. storeParts 정렬
# 2. 이진탐색 함수 정의
# 3. 탐색 수행 및 배열 생성