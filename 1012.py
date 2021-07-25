# 유기농 배추
"""
섬 영역, 음료수 얼려 먹기 등등...영역 구하는 문제와 유사한 것 같다.
인접 행렬 사용 !!
"""
import sys
sys.setrecursionlimit(10**6)
T = int(input())

def dfs(x,y):
    print("x =",x,"y =",y)
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    if field[x][y] == 1:
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

for _ in range(T):
    M, N, K = map(int, input().split())
    field = []
    for _ in range(K):
        X, Y = map(int, input().split())
        field[Y][X] = 1
    print(field)
    cnt = 0
    for n in range(N):
        for m in range(M):
            if dfs(n, m) == True:
                cnt += 1
    print(cnt)
