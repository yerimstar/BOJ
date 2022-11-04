# 그림
import sys
from collections import deque

def bfs(x,y):
    global cnt
    q = deque()
    q.append([x,y])
    visited[x][y] = True

    while q:
        x,y = q.popleft()
        cnt += 1
        for mx,my in move:
            dx = x + mx
            dy = y + my
            # 도화지 범위 내에 있는 지점인지 확인
            if 0 <= dx < n and 0 <= dy < m:
                # 색칠되어 있고 아직 방문하지 않은 지점
                if graph[dx][dy] and not visited[dx][dy]:
                    graph[dx][dy] = 0
                    visited[dx][dy] = True
                    q.append([dx, dy])
    return cnt

n,m = map(int,sys.stdin.readline().split())
graph = []
move = [[0, 1], [0, -1], [1, 0], [-1, 0]]
visited = [[False for _ in range(m)] for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

tmp = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            cnt = 0
            tmp.append(bfs(i,j))

if len(tmp) == 0:
    print(0)
    print(0)
else:
    print(len(tmp))
    print(max(tmp))