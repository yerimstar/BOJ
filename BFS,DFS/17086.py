# 아기 상어 2
import sys
from collections import deque

def bfs(sx,sy):
    visited = [[0 for _ in range(m)] for _ in range(n)]
    q = deque()
    q.append([sx,sy])
    visited[sx][sy] = 1
    distance[sx][sy] = 0
    while q:
        x,y = q.popleft()
        for mx,my in move:
            dx = x + mx
            dy = y + my
            if 0 <= dx < n and 0 <= dy < m:
                # 아기 상어가 없는 위치여야 함
                if graph[dx][dy] == 0 and not visited[dx][dy]:
                    q.append([dx,dy])
                    distance[dx][dy] = min(distance[x][y] + 1, distance[dx][dy])
                    visited[dx][dy] = 1

n,m = map(int,sys.stdin.readline().split())
graph = []
shark = []
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            shark.append([i,j])
move = [[-1,-1],[-1,0],[-1,1],[0,1],[0,-1],[1,-1],[1,0],[1,1]]
distance = [[10000 for _ in range(m)] for _ in range(n)]
for x,y in shark:
    bfs(x,y)

result = 0
for i in range(n):
    for j in range(m):
        result = max(result,distance[i][j])
print(result)
