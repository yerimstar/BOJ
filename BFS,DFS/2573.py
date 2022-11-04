# 빙산
import sys
from collections import deque
def bfs(sx,sy):
    q = deque()
    q.append([sx,sy])
    while q:
        print("q = ",q)
        visited = [[False for _ in range(m)] for _ in range(n)]
        x,y = q.popleft()
        visited[x][y] = True
        for mx,my in move:
            dx = x + mx
            dy = y + my
            if 0 <= dx < n and 0 <= dy < m:
                if not visited[dx][dy] and graph[dx][dy] == 0 and graph[x][y] > 1:
                    graph[x][y] -= 1
                if graph[dx][dy] == 0:
                    visited[dx][dy] = True
                if graph[dx][dy] != 0:
                    q.append([dx,dy])
        print(graph)

n,m = map(int,sys.stdin.readline().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))
for i in range(n):
    for j in range(m):
        if graph[i][j] != 0:
            sx,sy = i,j
move = [[0,1],[1,0],[-1,0],[0,-1]]
bfs(sx,sy)