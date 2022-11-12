# 치즈
import sys
from collections import deque

def bfs(x,y):
    visited = [[False for _ in range(m)] for _ in range(n)]
    q = deque()
    q.append([x,y])
    while q:
        x,y = q.popleft()
        visited[x][y] = True
        for mx,my in move:
            dx = x + mx
            dy = y + my
            if 0 <= dx < n and 0 <= dy < m:
                if not visited[dx][dy]:
                    if graph[dx][dy] == 1:
                        graph[dx][dy] = -1
                    elif graph[dx][dy] < 0:
                        graph[dx][dy] -= 1
                    elif graph[dx][dy] == 0:
                        q.append([dx, dy])
                        visited[dx][dy] = True
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] <= -2:
                graph[i][j] = 0
            elif graph[i][j] == -1:
                graph[i][j] = 1

            if graph[i][j] == 1:
                cnt += 1
    return cnt

n,m = map(int,sys.stdin.readline().split())
check = 0
graph = []
move = [[0,1],[0,-1],[1,0],[-1,0]]
for _ in range(n):
    tmp = list(map(int,sys.stdin.readline().split()))
    for i in range(m):
        if tmp[i] == 1:
            check += 1
    graph.append(tmp)

year = 0
while check != 0:
    cnt = bfs(0,0)
    check = cnt
    year += 1
print(year)

