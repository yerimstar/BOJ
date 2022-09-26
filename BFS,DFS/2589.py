# 보물섬
import sys
from collections import deque

h,w = map(int,sys.stdin.readline().split())
graph = [list(sys.stdin.readline().strip()) for _ in range(h)]

def bfs(i,j):
    visited = [[0 for _ in range(w)] for _ in range(h)]
    mv = [[0,1],[0,-1],[1,0],[-1,0]]
    queue = deque([(i,j)])
    visited[i][j] = 1
    while queue:
        x,y = queue.popleft()
        for mx,my in mv:
            dx = x + mx
            dy = y + my
            if 0 <= dx < h and 0 <= dy < w and graph[dx][dy] == 'L' and visited[dx][dy] == 0:
                queue.append([dx,dy])
                visited[dx][dy] = visited[x][y] + 1
    return max(map(max,visited))
result = 0
for i in range(h):
    for j in range(w):
        if graph[i][j] == 'L':
            num = bfs(i,j)
            if num > result:
                result = num
print(result-1)