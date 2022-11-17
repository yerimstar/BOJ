# 불!
import sys
from collections import deque

def bfs():
    while jihoon:
        if fire:
            for _ in range(len(fire)):
                x, y = fire.popleft()
                for mx, my in move:
                    dx = x + mx
                    dy = y + my
                    if 0 <= dx < r and 0 <= dy < c:
                        if graph[dx][dy] == '.':
                            graph[dx][dy] = 'F'
                            fire.append((dx, dy))
        if jihoon:
            for _ in range(len(jihoon)):
                sx, sy, cnt = jihoon.popleft()
                for mx, my in move:
                    dx = sx + mx
                    dy = sy + my
                    if 0 <= dx < r and 0 <= dy < c:
                        if not visited[dx][dy] and graph[dx][dy] == '.':
                            jihoon.append((dx, dy, cnt + 1))
                            visited[dx][dy] = True
                    else:
                        return cnt + 1
    return 0

r,c = map(int,sys.stdin.readline().split())
graph = []
move = [[0,1],[0,-1],[1,0],[-1,0]]
fire = deque()
jihoon = deque()
visited = [[False for _ in range(c)] for _ in range(r)]

for i in range(r):
    tmp = list(sys.stdin.readline().strip())
    for j in range(c):
        if tmp[j] == 'J':
            jihoon.append((i, j, 0))
            visited[i][j] = True
            tmp[j] = '.'
        elif tmp[j] == 'F':
            fire.append((i,j))
    graph.append(tmp)

result = bfs()

if result == 0:
    print("IMPOSSIBLE")
else:
    print(result)

