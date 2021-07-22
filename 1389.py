# 케빈 베이컨의 6단계 법칙
# 1차 아이디어
"""
각 연결된 값들 그래프로 만들기 -> 이중 리스트
BFS활용 -> deque -> popleft할 때마다 cnt 1증가 , 찾아야 하는 값 만나면 멈춤
유저수 N개 -> 1~N까지 BFS 테스트했을 때 합이 최소인 유저 구하기
"""
import sys
from collections import deque
N,M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A,B = map(int,sys.stdin.readline().split())
    graph[A].append(B)
    graph[B].append(A)

def bfs(start):
    queue = deque()
    visited = [start]
    count = []
    queue.append([start,1])

    while queue:
        node,cnt = queue.popleft()
        for i in range(len(graph[node])):
            if graph[node][i] not in visited:
                queue.append([graph[node][i],cnt+1])
                visited.append(graph[node][i])
                count.append(cnt)

    sum_count = sum(count)
    return sum_count

counts = []
for i in range(1,N+1):
    val = bfs(i)
    counts.append(val)
print(counts.index(min(counts))+1)