# 데스 나이트
import sys
from collections import deque
def bfs(x,y):
    q = deque()
    q.append([x,y])
    visited[x][y] = 1
    while q:
        x,y = q.popleft()
        for mx,my in move:
            dx = x + mx
            dy = y + my
            if 0 <= dx < n and 0 <= dy < n:
                if not visited[dx][dy]:
                    visited[dx][dy] = visited[x][y] + 1
                    q.append([dx, dy])
    return
n = int(sys.stdin.readline())
r1,c1,r2,c2 = map(int,sys.stdin.readline().split())
graph = [[0 for _ in range(n)] for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
move = [[-2,-1],[-2,1],[0,-2],[0,2],[2,-1],[2,1]]
graph[r1][c1] = 1
graph[r2][c2] = 1
bfs(r1,c1)
print(visited[r2][c2]-1)