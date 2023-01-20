# 점프
# 경로 찾는 문제랑 유사...이전 값들을 저장해두기!
import sys
N = int(sys.stdin.readline())
board = []
visited = [[0]*N for _ in range(N)]
visited[0][0] = 1

for i in range(N):
    board.append(list(map(int,sys.stdin.readline().split())))

for i in range(N):
    for j in range(N):
        if i == N-1 and j == N-1:
            break
        right = j + board[i][j]
        down = i + board[i][j]
        # 범위 체크
        if right < N:
            visited[i][right] += visited[i][j]
        if down < N:
            visited[down][j] += visited[i][j]

print(visited[i][j])
