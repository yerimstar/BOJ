# 섬의 개수
'''
음료수 얼려먹기 문제랑 비슷함...
Land = 1 Sea = 0
Land가 연결되어 있는 묶음을 찾는 문제임
'''
import sys
sys.setrecursionlimit(10**6)
move = [[-1,1],[-1,0],[-1,-1],[0,1],[0,-1],[1,1],[1,0],[1,-1]]
def DFS(x,y):
    if x < 0 or x >= H or y < 0 or y >= W:
        return False
    if Map[x][y] == 1:
        Map[x][y] = 0
        for i in range(8):
            dx = x + move[i][0]
            dy = y + move[i][1]
            DFS(dx, dy)
        return True
    return False

while(1):
    W, H = map(int, input().split())
    if W == 0 and H == 0:
        exit()
    Map = []
    for h in range(H):
        Map.append(list(map(int, input().split())))
    island = 0
    for h in range(H):
        for w in range(W):
            if DFS(h,w) == True:
                island += 1
    print(island)
