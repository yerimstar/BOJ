# 알파벳
import sys

def dfs(graph,y,x):
    if y <= -1 or y >= R or x <= -1 or x >= C:
        return False
    if graph[y][x] != 1 and graph[y][x] not in lst:
        lst.append(graph[y][x])
        graph[y][x] = 1
    else:
        return False
    move = [[0,-1],[0,1],[-1,0],[1,0]]
    for my,mx in move:
        dy = y + my
        dx = x + mx
        dfs(graph,dy,dx)

R,C = map(int,sys.stdin.readline().split())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
lst = []
dfs(graph,0,0)
print(len(lst))