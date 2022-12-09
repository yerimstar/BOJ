# 오르막 수
import sys
n = int(sys.stdin.readline())
dp = [[0 for _ in range(10)] for _ in range(n+1)]
for i in range(10):
    dp[0][i] = 1
for i in range(n+1):
    for j in range(10):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
print(dp[n][9]%10007)