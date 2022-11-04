# 그림
import sys
def dfs(x,y):
    global cnt
    move = [[0,1],[0,-1],[1,0],[-1,0]]
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        cnt += 1
        for mx, my in move:
            dx = x + mx
            dy = y + my
            dfs(dx, dy)
        return True
    return False

n,m = map(int,sys.stdin.readline().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

tmp = []
for i in range(n):
    for j in range(m):
        cnt = 0
        if dfs(i,j) and cnt != 0:
            tmp.append(cnt)

if len(tmp) == 0:
    print(0)
    print(0)
else:
    print(len(tmp))
    print(max(tmp))