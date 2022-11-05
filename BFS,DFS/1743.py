# 음식물 피하기
import sys
from collections import deque
def bfs(x,y):
    global cnt
    q = deque()
    q.append([x,y])
    visited[x][y] = True
    while q:
        x,y = q.popleft()
        for mx,my in move:
            dx = x + mx
            dy = y + my
            if 0 <= dx < n and 0 <= dy < m:
                if graph[dx][dy] == 1 and not visited[dx][dy]:
                    cnt += 1
                    q.append([dx,dy])
                    visited[dx][dy] = True
    return cnt

n,m,k = map(int,sys.stdin.readline().split())
graph = [[0 for _ in range(m)] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
move = [[0,1],[1,0],[0,-1],[-1,0]]
for _ in range(k):
    r,c = map(int,sys.stdin.readline().split())
    graph[r-1][c-1] = 1
tmp = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            cnt = 1
            cnt = bfs(i, j)
            tmp.append(cnt)
print(max(tmp))