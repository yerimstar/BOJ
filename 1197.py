# 최소 스패닝 트리 = 최소 신장 트리
def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b: # 더 작은 값이 루트 노드가 됨
        parent[b] = a
    else:
        parent[a] = b

V, E = map(int,input().split()) # V = 정점, E = 간선
parent = [0] * (V+1) # 부모 테이블 초기화

edges = []
result = 0

for i in range(1,V+1):
    parent[i]  = i # 부모 테이블을 자기 자신으로 초기화
for _ in range(E):
    A,B,C = map(int,input().split())
    edges.append((C,A,B)) # 가중치 기준으로 정렬하기 위해 가중치를 1번째 원소로 지정

edges.sort()

for edge in edges:
    C,A,B = edge
    if find_parent(parent,A) != find_parent(parent,B): #사이클 아닌 경우
        union_parent(parent,A,B)
        result += C

print(result)


