# 적록색약
import sys
sys.setrecursionlimit(10**6)

def dfs(c,graph,y,x,visited):
    for my, mx in move:
        dy = y + my
        dx = x + mx
        if dx <= -1 or dx >= n or dy <= -1 or dy >= n:
            continue
        if visited[dy][dx] == 0:
            if c == 'RG' and (graph[dy][dx] == 'R' or graph[dy][dx] == 'G'):
                visited[dy][dx] = 1
                dfs(c, graph, dy, dx, visited)
            elif graph[dy][dx] == c:
                visited[dy][dx] = 1
                dfs(c,graph,dy,dx,visited)

n = int(sys.stdin.readline())

graph = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
RG_visited = [[0 for _ in range(n)] for _ in range(n)]
result = 0
RG_result = 0

move = [[1,0],[-1,0],[0,1],[0,-1]]

for c in ['R','G','B']:
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j] == c:
                visited[i][j] = 1
                dfs(c, graph, i, j, visited)
                result += 1

for c in ['RG','B']:
    for i in range(n):
        for j in range(n):
            if not RG_visited[i][j]:
                if c == 'RG'and (graph[i][j] == 'R' or graph[i][j] == 'G'):
                    RG_visited[i][j] = 1
                    dfs(c, graph, i, j, RG_visited)
                    RG_result += 1
                elif c == 'B':
                    RG_visited[i][j] = 1
                    dfs(c, graph, i, j, RG_visited)
                    RG_result += 1

print(result,RG_result)