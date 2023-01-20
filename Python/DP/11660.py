# 구간 합 구하기 5
import sys
n,m = map(int,sys.stdin.readline().split())
lst = []
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(n):
    lst.append(list(map(int,sys.stdin.readline().split())))
for i in range(n):
    for j in range(n):
        dp[i+1][j+1] = dp[i][j+1] + dp[i+1][j] - dp[i][j] + lst[i][j]
for _ in range(m):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
    print(dp[x2][y2]-dp[x1-1][y2]-dp[x2][y1-1]+dp[x1-1][y1-1])