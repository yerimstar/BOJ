# 알파벳
import sys
sys.setrecursionlimit(10**6)
def dfs(graph,y,x,visited,move):
    # 방문한적 없는 알파벳인 경우
    if not visited[y][x] and graph[y][x] not in lst:
        lst.append(graph[y][x])
        visited[y][x] = 1
    # 방문한적 있거나 방문했던 알파벳인 경우
    else:
        return False
    # 상하좌우
    for my,mx in move:
        dy = y + my
        dx = x + mx
        # 범위 안에 존재하는지 검사
        if dy <= -1 or dy >= R or dx <= -1 or dx >= C:
            continue
        dfs(graph,dy,dx,visited,move)

R,C = map(int,sys.stdin.readline().split())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
# 좌측 상단에서 시작 (0,0)

move1 = [[0, -1], [0, 1], [-1, 0], [1, 0]]
move2 = [[-1,0],[1,0],[0,-1],[0,1]]
result = 0
for move in [move1,move2]:
    lst = []
    visited = [[0 for _ in range(C)] for _ in range(R)]
    dfs(graph,0,0,visited,move)
    result = max(result,len(lst))
print(result)