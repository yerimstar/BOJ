# DFS와 BFS
from collections import deque
N,M,V = map(int,input().split())

def dfs(graph,start,visited):
    # 처음 시작 노드 방문 처리
    visited[start] = True
    print(start,end=' ')
    # 해당 노드와 인접한 노드 방문처리
    if len(graph[start]) >= 2:
        graph[start].sort()
    for i in graph[start]:
        if visited[i] == False:
            # 방문처리
            visited[i] = True
            # 재귀적으로 dfs 호출
            dfs(graph,i,visited)

def bfs(graph,start,visited):
    queue = deque()
    queue.append(start)
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        if len(graph[v]) >= 2:
            graph[v].sort()
        for i in graph[v]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

graph = [[] for _ in range(N+1)]
# 간선의 개수만큼 추가
for _ in range(M):
    a,b = map(int,input().split())
    # 양방향 연결
    graph[a].append(b)
    graph[b].append(a)

visited = [False for _ in range(N+1)]
dfs(graph,V,visited)
print()
visited = [False for _ in range(N+1)]
bfs(graph,V,visited)