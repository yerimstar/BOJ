# 다리 놓기
import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n,m = map(int,sys.stdin.readline().split())
    dp = [[0 for _ in range(m+1)] for _ in range(m+1)]
    for i in range(m+1):
        for j in range(m+1):
            if j == 0:
                dp[i][j] = 1
            else:
                if i == j:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
    print(dp[m][n])