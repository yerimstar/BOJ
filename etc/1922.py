# 네트워크 연결
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

N = int(input())
M = int(input())
parent = [0] * (N+1) # 부모 테이블 초기화

edges = []
result = 0

for i in range(1,N+1):
    parent[i] = i

for _ in range(M):
    a,b,c = map(int,input().split())
    edges.append((c,a,b))

edges.sort()

for edge in edges:
    c,a,b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += c

print(result)