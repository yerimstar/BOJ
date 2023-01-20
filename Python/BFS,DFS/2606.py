# 바이러스
n = int(input())
m = int(input())

def dfs(graph,start,visited):
    global result
    # 시작 노드 방문처리
    visited[start] = True
    for i in graph[start]:
        if visited[i] == False:
            # 방문처리
            visited[i] = True
            # 바이러스 걸림
            result += 1
            dfs(graph,i,visited)

# 컴퓨터수+1만큼 그래프 생성
graph = [[] for _ in range(n+1)]
# 간선이 어떤 노드와 연결되어 있는지 파악
for _ in range(m):
    a,b = map(int,input().split())
    # 양방향 연결
    graph[a].append(b)
    graph[b].append(a)

# 방문처리
visited = [False for _ in range(n+1)]
# 1번 컴퓨터로 인해 바이러스 걸리게 된 컴퓨터 수
result = 0
dfs(graph,1,visited)
print(result)
