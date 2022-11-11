# 치즈
import sys
from collections import deque

def bfs(x,y):
    cnt = 0
    visited = [[False for _ in range(m)] for _ in range(n)]
    q = deque()
    q.append([x,y])
    visited[x][y] = True
    while q:
        x,y = q.popleft()
        for mx,my in move:
            dx = x + mx
            dy = y + my
            if 0 <= dx < n and 0 <= dy < m:
                if not visited[dx][dy]:
                    visited[dx][dy] = True
                    if graph[dx][dy] == 0:
                        q.append([dx,dy])
                    elif graph[dx][dy] == 1:
                        graph[dx][dy] = 0
                        cnt += 1
    return cnt

n,m = map(int,sys.stdin.readline().split())
check = 0
graph = []
move = [[0,1],[1,0],[0,-1],[-1,0]]
for _ in range(n):
    tmp = list(map(int,sys.stdin.readline().split()))
    for i in range(m):
        if tmp[i] == 1:
            check += 1
    graph.append(tmp)

year = 0
while check != 0:
    year += 1
    cnt = bfs(0,0)
    check -= cnt

print(year)
print(cnt)
