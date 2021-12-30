# 최단경로
import sys
import heapq
INF = int(1e9)
V, E = map(int,sys.stdin.readline().split())
K = int(sys.stdin.readline())

# 그래프 표현
graph = [[] for _ in range(V+1)]
weight = [INF] * (V+1)
weight[K] = 0 # 시작노드는 자기자신이므로 가중치 값이 0이다

# 가중치 입력(입력값)
for _ in range(E):
    u,v,w = map(int,sys.stdin.readline().split())
    graph[u].append([w,v]) # 이웃 노드 저장

# heapq에 가중치 저장
heap = []
heapq.heappush(heap,[0,K]) # 시작노드의 가중치는 0

# 다익스트라 알고리즘
def dijkstra():
    while heap:
        now_weight,now  = heapq.heappop(heap) # 탐색할 노드, 가중치
        if weight[now] < now_weight: # 가중치 값 비교
            continue
        for new_weight,new in graph[now]:
            final_weight = now_weight + new_weight
            # 기존 가중치와 비교 후 새로 계산한 값이 더 작으면 값 업데이트
            if final_weight < weight[new]:
                weight[new] = final_weight
                heapq.heappush(heap,[final_weight,new])

dijkstra()

for i in range(1,V+1):
    if weight[i] == INF:
        print("INF")
    else:
        print(weight[i])
