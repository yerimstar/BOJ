# 유기농 배추
# 인접 행렬을 사용해야 할 것 같음
import sys
sys.setrecursionlimit(10**6)
def dfs(graph,y,x):
    # print("y = ",y,"x = ",x)
    if x <= -1 or x >= m or y <= -1 or y >= n:
        return False
    # print("graph[y][x] = ", graph[y][x])
    if graph[y][x] == 1:
        # 방문 처리
        graph[y][x] = 0
        dfs(graph,y,x-1)
        dfs(graph,y,x+1)
        dfs(graph,y-1,x)
        dfs(graph,y+1,x)
        return True
    return False
# 테스트 케이스
T = int(input())
for _ in range(T):
    # m = 배추밭 가로길이, n = 배추밭 새로길이, k = 배추가 심어져있는 위치 개수
    m,n,k = map(int,input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        a,b = map(int,input().split())
        graph[b][a] = 1
    result = 0
    for y in range(n):
        for x in range(m):
            if dfs(graph,y,x):
                result += 1
    print(result)

