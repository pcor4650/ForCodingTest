# 리스트 #

array = [i for i in range(20) if i%2==1]    #리스트 컴프리헨션# 0부터 19까지 홀수만 포함하는 리스트 생성

# 2차원 배열 정렬 
x = [[2, 1], [3, 4], [1, 2], [1, 3], [3, 2]]
x.sort(key=lambda x:x[0])   
결과 :  [[1, 2], [1, 3], [2, 1], [3, 4], [3, 2]] #0번째 인덱스 기준 오름차순 정렬, X[1]으로는 정렬되지 않음

x.sort(key=lambda x:(x[0], x[-1]))
결과 :  [[1, 3], [1, 2], [2, 1], [3, 4], [3, 2]] #0번째 인덱스 기준 정렬 후, 동일한 값의 경우 내림차순 정렬

x.sort()
결과 : [[1, 2], [1, 3], [2, 1], [3, 2], [3, 4]]   #0, 1번째 인덱스 모두에 대해 오름차순 정렬

# 2차원 배열 값 추출 
b = list()
b = sum(x, [])  #sum으로 2차원 리스트를 1차원 리스트로 변환

import itertools
b = list(itertools.chain(*x))   #itertools로 2차원 -> 1차원 변환

b = [data for innerList in x for data in innerList] #

for x1,x2 in x: #반복문으로 변환
    b.append(x1)
    b.append(x2)

# 2차원 배열 열 추출
c = [t[0] for t in x]    

# 2차원 리스트 각 행의 최대값을 찾는 방법
map(max, 리스트)

#주요 메서드
x = []
x.append(a)
x.sort()
x.reverse()  #리스트의 원소 순서를 모두 뒤집어 놓는다  O(N)
x.insert(삽입위치 인덱스, 삽입할 값)
x.count(특정 값) # 리스트에서 특정 값을 가지는 데이터의 개수를 셀 때
x.remove(특정 값) # 리스트에서 특정 값을 갖는 원소를 제거할 때, 값을 가진 원소가 여러개면 하나만 제거한다

# 2차원 행<->열 변환
a = [[3, 3, 1, 2], [1, 1, 3, 1], [3, 3, 1, 1], [1, 1, 3, 3]]
a_transpose = [col for col in zip(*a)]

# 배열 내 모든 값 특정 값으로 빼기
B = [4, 5, 8]
B = list(map(lambda x-B[0], B))

##################################################################################################################################
# 2차원에서 상,하,좌,우 이동방법
dx = [-1. 0, 1, 0]
dy = [0, -1, 0, 1]
 또는
dir = [[-1,0], [1,0], [0,-1], [0,1]]

# global 언제 사용?

# in 연산자와 not in 연산자, True 또는 False 반환
x in 리스트
x not in 문자열

# 사전 자료형 # 키-값 쌍을 데이터로 가지는 자료형
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

# 집합 자료형 # 리스트 중복 제거에 주로 사용, |, &, -
data = set([1,1,2,3,4,4,5])

# 입출력 속도 # 입력의 개수가 많을 경우 input() 사용 시 시간 초과 될 수 있다
input() < sys.stdin.readline()

#itertools#

from itertools import permutations
from itertools import combinations

data = ['A', 'B', 'C']
result = list(permutations(data, 3))
result = list(combinations(data, 2))