# 연결 요소의 개수
from collections import deque
def bfs(graph,v,visited):
    if visited[v] == True:
        return False
    visited[v] = True
    queue = deque()
    queue.append(v)
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == False:
                visited[i] = True
                queue.append(i)
    return True

n, m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False for _ in range(n+1)]
result = 0
for i in range(1,n+1):
    if bfs(graph,i,visited):
        result += 1
print(result)