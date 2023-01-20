# 바닥 장식
import sys
sys.setrecursionlimit(10**6)
def dfs(graph,y,x,visited):
    if x <= -1 or x >= m or y <= -1 or y >= n or visited[y][x]:
        return False
    visited[y][x] = True
    if graph[y][x] == '-':
        print("-")
        if graph[y][x-1] == '-':
            dfs(graph,y,x-1,visited)
        if graph[y][x+1] == '-':
            dfs(graph,y,x+1,visited)
        return True
    elif graph[y][x] == '|':
        print("|")
        if graph[y-1][x] == '|':
            dfs(graph, y - 1, x, visited)
        if graph[y+1][x] == '|':
            dfs(graph,y+1,x,visited)
        return True

n, m = map(int,sys.stdin.readline().split())
visited = [[False for _ in range(m)] for _ in range(n)]
graph = [[] for _ in range(n)]
for i in range(n):
    graph[i] = list(sys.stdin.readline().rstrip())

cnt = 0
for y in range(n):
    for x in range(m):
        print(y,x)
        if dfs(graph,y,x,visited):
            cnt += 1
print(cnt)