# 타일 장식물
import sys
n = int(sys.stdin.readline())
dp = [0] * 81
dp[1] = 1
dp[2] = 1
for i in range(3, n+1):
    dp[i] = dp[i-1]+dp[i-2]
result = (dp[n-1] + dp[n])*2 + dp[n]*2
print(result)