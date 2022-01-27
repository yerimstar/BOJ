# 인구 이동
import sys
from collections import deque

graph = []
n,l,r = map(int,sys.stdin.readline().split())
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(y,x):
    dq = deque()
    tmp = []
    dq.append((y,x))
    tmp.append((y,x))
    people = 0
    cnt = 0
    visited[y][x] = True
    while dq:
        y,x = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx]:
                if l <= abs(graph[ny][nx]-graph[y][x]) <= r:
                    visited[ny][nx] = True
                    dq.append((ny, nx))
                    tmp.append((ny,nx))
    return tmp

day = 0
while True:
    visited = [[False] * n for _ in range(n)]
    check = False
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False:
                visited[i][j] == True
                tmp = bfs(i,j)
                if len(tmp) > 1:
                    check = True
                    num = 0
                    for y,x in tmp:
                        num += graph[y][x]
                    num = num // len(tmp)

                    for y,x in tmp:
                        graph[y][x] = num
    if not check:
        break
    day += 1

print(day)