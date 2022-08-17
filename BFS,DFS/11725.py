# 트리의 부모 찾기
import sys
from collections import deque

def bfs(start,visited,parent):
    queue = deque()
    queue.append(start)
    visited[start] = 1
    while queue:
        val = queue.popleft()
        for node in graph[val]:
            if not visited[node]:
                visited[node] = 1
                queue.append(node)
                parent[node] = val

n = int(sys.stdin.readline())

# n-1개 줄에 연결 노드 입력
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0 for _ in range(n+1)]
parent = [0 for _ in range(n+1)]
bfs(1,visited,parent)
for i in range(2,n+1):
    print(parent[i])