# 양치기 꿍
"""
R = 세로의 길이, C = 가로의 길이
. = 빈공간 , # = 울타리, v = 늑대, k = 양

"""
import sys
sys.setrecursionlimit(10**6)

R,C = map(int,input().split())
field = []
for r in range(R):
    field.append(list(map(str,input())))
print(field)

move = [[-1,0],[1,0],[0,-1],[0,1]]
def dfs(x,y,k,v):
    print("x =",x,"y =",y)
    print("field =",field[x][y])
    if x < 0 or x >= C or y < 0 or y >= R:
        return k,v
    if field[x][y] == 'k':
        field[x][y] = '#'
        for i in range(4):
            dx = x + move[i][0]
            dy = y + move[i][1]
            dfs(dx, dy,k,v)
        k += 1
    elif field[x][y] == 'v':
        field[x][y] = '#'
        for i in range(4):
            dx = x + move[i][0]
            dy = y + move[i][1]
            dfs(dx, dy,k,v)
        v += 1
    return k,v

lamb = 0
wolf = 0
for r in range(R):
    for c in range(C):
        k = 0
        v = 0
        k,v = dfs(r,c,k,v)
        if k != 0:
            lamb += k
        if wolf != 0:
            wolf += c

print(lamb,wolf)