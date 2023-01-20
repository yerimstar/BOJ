# 책 - DFS 실전문제
import sys
N,M = map(int,sys.stdin.readline().split())
graph = []
for i in range(N):
    graph.append(list(map(int,input())))

move = [[0,1],[0,-1],[1,0],[-1,0]]
def dfs(x,y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        for i in range(4):
            dx = x + move[i][0]
            dy = y + move[i][1]
            dfs(dx,dy)
        return True
    return False

result = 0
for n in range(N):
    for m in range(M):
        if dfs(n,m) == True:
            result += 1
print(result)
