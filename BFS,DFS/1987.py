# 알파벳
import sys

def dfs(graph,y,x,visited):
    print("y = ",y,"x = ",x)
    # 범위 안에 존재하는지 검사
    if y <= -1 or y >= R or x <= -1 or x >= C:
        return False
    # 방문한적 없는 알파벳인 경우
    if not visited[y][x] and graph[y][x] not in lst:
        lst.append(graph[y][x])
        visited[y][x] = 1
    # 방문한적 있거나 방문했던 알파벳인 경우
    else:
        return False
    # 상하좌우
    move = [[0,-1],[0,1],[-1,0],[1,0]]
    for my,mx in move:
        dy = y + my
        dx = x + mx
        print("dy = ",dy,"dx = ",dx)
        dfs(graph,dy,dx,visited)

R,C = map(int,sys.stdin.readline().split())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
visited = [[0 for _ in range(C)] for _ in range(R)]
lst = []
# 좌측 상단에서 시작 (0,0)
dfs(graph,0,0,visited)
print(graph)
print(len(lst))