# 이친수
import sys
from itertools import product

n = int(sys.stdin.readline())
dp = [[0,0,0] for _ in range(91)]
dp[1] = [0,1,1]
dp[2] = [1,0,1]
dp[3] = [1,1,2]
dp[4] = [2,1,3]
for i in range(5,n+1):
    dp[i][0] = dp[i-1][0]+dp[i-1][1]
    dp[i][1] = dp[i-1][0]
    dp[i][2] = dp[i][0]+dp[i][1]
print(dp[n][2])
