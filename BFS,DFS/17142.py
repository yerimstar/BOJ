# 연구소 3
import sys
from collections import deque
from itertools import combinations

def bfs(v):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    q = deque()
    tmp_graph = [x[:] for x in graph]
    for x,y in v:
        q.append([x,y])
        visited[x][y] = 1
        tmp_graph[x][y] = 0
    while q:
        x,y = q.popleft()
        for mx,my in move:
            dx = x + mx
            dy = y + my
            if 0 <= dx < n and 0 <= dy < n:
                if not visited[dx][dy] and tmp_graph[dx][dy] == 0:
                    visited[dx][dy] = 1
                    tmp_graph[dx][dy] = tmp_graph[x][y] + 1
                    q.append([dx,dy])
    cnt = 0
    for i in range(n):
        for j in range(n):
            if tmp_graph[i][j] == '*':
                tmp_graph[i][j] = 0
    if cnt == 0:
        for i in range(n):
            cnt = max(cnt,max(tmp_graph[i]))
        return cnt
    else:
        return -1

n,m = map(int,sys.stdin.readline().split())
graph = []
virus = []
empty = 0
move = [[1,0],[0,1],[-1,0],[0,-1]]
for i in range(n):
    tmp = list(map(int,sys.stdin.readline().split()))
    for j in range(n):
        if tmp[j] == 2:
            tmp[j] = '*'
            virus.append([i,j])
        elif tmp[j] == 0:
            empty += 1
    graph.append(tmp)
virus_lst = list(combinations(virus,m))
result = 10**6
if empty == 0:
    result = 0
else:
    for v in virus_lst:
        cnt = bfs(v)
        if cnt != -1:
            result = min(result,cnt)
    if result == 10**6:
        result = -1

print(result)
