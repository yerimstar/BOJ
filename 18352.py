# 특정 거리의 도시 찾기
import sys
from collections import deque

N,M,K,X = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    A,B = map(int,sys.stdin.readline().split())
    graph[A].append(B)

visited = [False] * (N+1)
check = 0

def shortdistance(graph,K,X):
    global check
    queue = deque()
    queue.append((X,0))
    while queue:
        node,distance = queue.popleft()
        if distance == K:
            print(node)
            check += 1
        elif distance < K:
            for g in graph[node]:
                if not visited[g]:
                    visited[g] = True
                    queue.append((g,distance + 1))

shortdistance(graph,K,X)
if check == 0:
    print("-1")