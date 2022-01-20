# 특정 거리의 도시 찾기
import sys
from collections import deque

N,M,K,X = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    A,B = map(int,sys.stdin.readline().split())
    graph[A].append(B)

def shortdistance(graph,K,X):
    result = []
    queue = deque()
    visited = [False] * (N + 1)

    queue.append((X,0))
    while queue:
        node,distance = queue.popleft()
        visited[node] = True
        if distance == K:
            result.append(node)
        elif distance < K:
            for g in graph[node]:
                if not visited[g]:
                    visited[g] = True
                    queue.append((g,distance + 1))
    if len(result) == 0:
        print("-1")
    else:
        result.sort()
        for i in range(len(result)):
            print(result[i])

shortdistance(graph,K,X)
