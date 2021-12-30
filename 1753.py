# 최단경로
INF = 56
V, E = map(int,input().split())
K = int(input())

# 그래프 표현
graph = [[] for _ in range(V+1)]
visited = [False] * (V+1)
weight = [INF] * (V+1)

# 가중치 입력
for _ in range(E):
    u,v,w = map(int,input().split())
    graph[u].append((v,w)) # 이웃 노드 저장

# 최단 거리 노드 찾는 함수
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1,V+1): # 1번째 노드부터 탐색하며 최단거리 노드를 찾는다.
        if not visited[i] and weight[i] < min_value: # 아직 방문하지 않은 노드이면서 최단거리인 노드
            min_value = weight[i]
            index = i
    return index

# 다익스트라 알고리즘
def dijkstra(K):
    # 시작노드
    weight[K] = 0 # 자기자신의 가중치는 0
    visited[K] = True # 방문처리
    # 시작노드와 인접한 노드들의 최단거리 계산
    for g in graph[K]:
        weight[g[0]] = g[1]
    # 시작노드를 제외한 다른 노드들 처리 -> V-1 개
    for _ in range(V-1):
        now = get_smallest_node()
        visited[now] = True # 방문처리
        # 해당노드의 인접한 노드들의 가중치 계산
        for g in graph[now]:
            w = weight[now] + g[1]
            # 기존 가중치와 비교 후 새로 계산한 값이 더 작으면 값 업데이트
            if w < weight[g[0]]:
                weight[g[0]] = w
dijkstra(K)

for i in range(1,V+1):
    if weight[i] == INF:
        print("INF")
    else:
        print(weight[i])
