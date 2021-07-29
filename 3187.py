# 양치기 꿍
"""
R = 세로의 길이, C = 가로의 길이
. = 빈공간 , # = 울타리, v = 늑대, k = 양
"""
import sys
sys.setrecursionlimit(10**6)

R,C = map(int,input().split())
land = []
for r in range(R):
    land.append(list(input()))

move = [[-1,0],[1,0],[0,-1],[0,1]]

def dfs(x,y):
    global k,v # 전역변수 선언
    if land[x][y] == 'k':
        k += 1
    elif land[x][y] == 'v':
        v += 1
    if land[x][y] != '#':
        land[x][y] = '#'
        for i in range(4):
            dx = x + move[i][0]
            dy = y + move[i][1]
            if dx < 0 or dx >= R or dy < 0 or dy >= C:
                continue
            if land[dx][dy] != '#':
                dfs(dx, dy)

lamb ,wolf = 0, 0
for r in range(R):
    for c in range(C):
        k, v = 0, 0
        dfs(r, c)
        if k > v:
            lamb += k
        else:
            wolf += v

print(lamb,wolf)