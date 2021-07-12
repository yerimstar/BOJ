import sys

N,M,V = map(int,sys.stdin.readline().split())
graph = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    m1,m2 = map(int,sys.stdin.readline().split())
    graph[m1][m2] = graph[m2][m1] = 1
print(graph)