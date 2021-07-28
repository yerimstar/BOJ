# 안전 영역
"""
N = 지역의 높이 정보
-> NxN 행렬
(N-1)이하인 값 -> 1
나머지 -> 0
=> 섬의 영역 문제랑 비슷함..
"""
import copy
import sys
sys.setrecursionlimit(10**6)

N = int(input())
land = []
num = 0
for _ in range(N):
    tmp = list(map(int,input().split()))
    land.append(tmp)
    if num < max(tmp):
        num = max(tmp)

move = [[1,0],[-1,0],[0,1],[0,-1]]
def dfs(tmp,x,y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    if tmp[x][y] == 0:
        tmp[x][y] = 1
        for i in range(4):
            dx = x + move[i][0]
            dy = y + move[i][1]
            dfs(tmp,dx,dy)
        return True
    return False

check = []
for n in range(num+1):
    tmp = copy.deepcopy(land)
    for i in range(N):
        for j in range(N):
            if tmp[i][j] <= n:
                tmp[i][j] = 1
            else:
                tmp[i][j] = 0
    cnt = 0
    for x in range(N):
        for y in range(N):
            if dfs(tmp,x, y) == True:
                cnt += 1
    check.append(cnt)

print(max(check))
