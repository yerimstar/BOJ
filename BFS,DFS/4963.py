# 섬의 개수
import sys
sys.setrecursionlimit(10**6)
def dfs(graph,y,x):
    graph[y][x] = 0
    for j in range(y - 1, y + 2):
        for i in range(x - 1, x + 2):
            if i <= -1 or i >= w or j <= -1 or j >= h:
                continue
            if graph[j][i] == 1:
                dfs(graph, j, i)
while True:
    w,h = map(int,sys.stdin.readline().split())
    if w + h == 0:
        break
    graph = []
    for i in range(h):
        graph.append(list(map(int,sys.stdin.readline().split())))
    island = 0
    for y in range(h):
        for x in range(w):
            if graph[y][x] == 1:
                dfs(graph,y,x)
                island += 1
    print(island)