# 효율적인 해킹
import sys
sys.setrecursionlimit(10**6)
def dfs(graph,start,visited):
    global cnt
    if visited[start]:
        return False
    for g in graph[start]:
        if not visited[g]:
            dfs(graph, g, visited)
            cnt += 1
            visited[g] = 1
            return True

N,M = map(int,sys.stdin.readline().split())
# N(컴퓨터수)+1만큼 생성
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,sys.stdin.readline().split())
    # A가 B를 신뢰한다 -> B를 해킹하면 A도 해킹할 수 있다.
    graph[b].append(a)

result = []
max_cnt = 0
for i in range(1,N+1):
    cnt = 1
    visited = [0] * (N+1)
    dfs(graph,i,visited)
    result.append([i,cnt])
    max_cnt = max(cnt,max_cnt)

for a,b in result:
    if b == max_cnt:
        print(a,end=' ')

