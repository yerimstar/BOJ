# 빙산
import sys
from collections import deque
import copy

def bfs(x,y):
    global check,graph
    tmp = copy.deepcopy(graph)
    cnt = 1
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
                if not visited[dx][dy] and graph[dx][dy]:
                    cnt += 1
                    q.append([dx,dy])
                    visited[dx][dy] = True
                elif graph[dx][dy] == 0:
                    tmp[x][y] -= 1
        if tmp[x][y] <= 0:
            tmp[x][y] = 0
            # print("x,y", x, y)
            check -= 1
    # print("tmp = ",tmp)
    graph = tmp
    # print("graph after = ",graph)
    return cnt

n,m = map(int,sys.stdin.readline().split())
graph = []
move = [[0,1],[0,-1],[1,0],[-1,0]]
check = 0
for _ in range(n):
    tmp = list(map(int,sys.stdin.readline().split()))
    for j in range(m):
        if tmp[j]:
            check += 1
    graph.append(tmp)
# print(graph)
# print(check)
num = 0
tmp = check
for i in range(n):
    for j in range(m):
        if graph[i][j]:
            cnt = bfs(i,j)
            if cnt == 0:
                print(0)
                exit()
            if cnt != tmp:
                print(num)
                exit()
            tmp = check
            num += 1
