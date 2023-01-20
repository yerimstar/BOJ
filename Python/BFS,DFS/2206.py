# 벽 부수고 이동하기
# 입력
import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().strip())) for _ in range(n)]
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
# 함수
def bfs():
    q = deque()
    # x, y, crashed
    q.append((0,0,0))
    # 방문처리 - 시작칸 포함
    visited[0][0][0] = 1
    while q:
        x,y,crashed = q.popleft()
        # 끝나는 칸 도착
        if x == n-1 and y == m-1:
            return visited[x][y][crashed]
        for i in range(4):
            dx = x + move[i][0]
            dy = y + move[i][1]
            # 맵 안에 존재하는지 검사
            if dx < 0 or dx >= n or dy < 0 or dy >= m:
                continue
            # 벽이 아니고, 방문하기 전인 상황
            if graph[dx][dy] == 0 and visited[dx][dy][crashed] == 0:
                visited[dx][dy][crashed] = visited[x][y][crashed] + 1
                q.append((dx,dy,crashed))
            # 벽이고, 벽을 아직 안 부순 상황
            elif graph[dx][dy] == 1 and crashed == 0:
                visited[dx][dy][1] = visited[x][y][crashed] + 1
                q.append((dx,dy,1))
    return -1


# 출력
move = [[0,1],[0,-1],[1,0],[-1,0]]
print(bfs())