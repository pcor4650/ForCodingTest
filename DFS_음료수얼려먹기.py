#N, M 공백으로 구분하여 입력 받ㅣ
n, m = map(int, input().split())

#2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(map(int,input()))
    
# DFS로 특정한 노드를 방문한 뒤 연결된 모든 노드들도 방문
def dfs(x, y):
    #주어진 범위를 벗어나는 경우에는 즉시 종료
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    #현재 노드를 방문하지 않았다면
    if graph[x][y] == 0:
        #방문처리 해주고
        graph[x][y] = 1
        #상, 하, 좌, 우 인접노드에 대해 모두 재귀적으로 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

result = 0
#모든 위치에 대해 dfs확인
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True :
            result += 1

print(result)


#문제 이코테 149p
