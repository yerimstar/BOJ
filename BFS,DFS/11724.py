# 연결 요소의 개수
from collections import deque
import sys

def bfs(graph,start,visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n, m = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False for _ in range(n+1)]
result = 0
for i in range(1,n+1):
    if not visited[i]:
        bfs(graph, i, visited)
        result += 1
print(result)