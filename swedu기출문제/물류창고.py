import sys
input = sys.stdin.readline
INF = 987654321

def floyd_warshall(N, M, board):
    for k in range(1, N+1): # 중간지점을 기준으로
        for i in range(1, N+1): # 출발
            for j in range(1, N+1): # 도착
                if i == j:
                    board[i][j] = 0
                board[i][j] = min(board[i][j], board[i][k]+board[k][j]) # i에서 j로 가는 최단거리를 i에서 k를 거쳐 j로 가는 최단거리로 갱신
    return board

def get_max_len(board):
    max_len = []
    for i in range(1, N+1):
        m = 0
        for j in range(1, N+1):
            m = max(m, board[i][j])
        max_len.append(m)
    return max_len

def solution(N, M, board):
    board = floyd_warshall(N, M, board)
    max_len = get_max_len(board)
    print(min(max_len))

N, M = map(int, input().split())
board = [[INF]*(N+1) for _ in range(N+1)]

for _ in range(M):
    y, x, d = map(int, input().split())
    board[y][x] = d
    board[x][y] = d

solution(N, M, board)