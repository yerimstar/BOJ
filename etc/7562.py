# 나이트의 이동
import sys
from collections import deque
T = int(sys.stdin.readline()) # test case의 개수

dx = [-1,-2,-1,-2,1,2,1,2]
dy = [2,1,-2,-1,2,1,-2,-1]

def bfs(graph,sx,sy,ex,ey):
    queue = deque()
    queue.append((sx,sy))

    while queue:
        tx,ty = queue.popleft()
        for i in range(8):
            x = tx+dx[i]
            y = ty+dy[i]
            if x < 0 or x >= L or y < 0 or y >= L:
                continue
            if graph[x][y] == 0:
                graph[x][y] = graph[tx][ty] + 1
                queue.append((x,y))
    return graph[ex][ey]

for _ in range(T):
    L = int(sys.stdin.readline()) # 체스판의 한 변의 길이
    graph = [[0] * L for _ in range(L)]
    sx,sy = map(int,sys.stdin.readline().split())
    ex,ey = map(int,sys.stdin.readline().split())
    if sx == ex and sy == ey:
        print("0")
    else:
        print(bfs(graph,sx,sy,ex,ey))
