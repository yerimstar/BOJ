# 전쟁 - 전투
import sys
from collections import deque
def bfs(x,y,check):
    cnt_b = 1
    cnt_w = 1
    q = deque()
    q.append([x,y])
    visited[x][y] = True
    while q:
        x,y = q.popleft()
        for mx,my in move:
            dx = x + mx
            dy = y + my
            if 0 <= dx < n and 0 <= dy < m:
                if check == 'W' and not visited[dx][dy] and graph[dx][dy] == 'W':
                    cnt_w += 1
                    q.append([dx,dy])
                    visited[dx][dy] = True
                elif check == 'B' and not visited[dx][dy] and graph[dx][dy] == 'B':
                    cnt_b += 1
                    q.append([dx,dy])
                    visited[dx][dy] = True
    if check == 'W':
        return cnt_w**2
    elif check == 'B':
        return cnt_b**2

n,m = map(int,sys.stdin.readline().split())
graph = []
visited = [[False for _ in range(m)] for _ in range(n)]
move = [[0,1],[0,-1],[1,0],[-1,0]]
for _ in range(n):
    graph.append(list(sys.stdin.readline().strip()))
white = []
blue = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'W' and not visited[i][j]:
            white.append(bfs(i,j,'W'))
        elif graph[i][j] == 'B' and not visited[i][j]:
            blue.append(bfs(i,j,'B'))

print(sum(white),sum(blue))