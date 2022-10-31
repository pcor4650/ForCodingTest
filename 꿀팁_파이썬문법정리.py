# 리스트 #

array = [i for i in range(20) if i%2==1]    #0부터 19까지 홀수만 포함하는 리스트

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

# in 연산자와 not in 연산자, True 또는 False 반환
x in 리스트
x not in 문자열




# 사전 자료형, 키-값 쌍을 데이터로 가지는 자료형
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

# 집합 자료형, 리스트 중복 제거에 주로 사용, |, &, -
data = set([1,1,2,3,4,4,5])

# 입출력 속도, 입력의 개수가 많을 경우 input() 사용 시 시간 초과 될 수 있다
input() < sys.stdin.readline()

#itertools

from itertools import permutations
from itertools import combinations

data = ['A', 'B', 'C']
result = list(permutations(data, 3))
result = list(combinations(data, 2))