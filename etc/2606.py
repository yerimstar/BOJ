# 바이러스
"""
인접 리스트 활용하여 시작 노드와 연결된 노드의 수를 구해주면 됨
-> DFS, BFS 둘다 가능
"""
import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline()) # 컴퓨터의 수
E = int(sys.stdin.readline()) # 컴퓨터 쌍의 수
computer = [[] for _ in range(N+1)]
for i in range(E):
    n1,n2 = map(int,sys.stdin.readline().split())
    computer[n1].append(n2)
    computer[n2].append(n1)

visited = []
def dfs(start):
    if start not in visited:
        visited.append(start)
        lst = computer[start]
        for l in lst:
            dfs(l)
dfs(1)
print(len(visited)-1) # 바이러스에 걸린 컴퓨터의 수이므로 시작 노드는 제외시켜야 함