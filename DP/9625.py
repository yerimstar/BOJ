# BABBA
import sys
k = int(sys.stdin.readline())

dp = [(0,0) for _ in range(46)]
dp[0] = (1,0)
for i in range(1,46):
    a,b = dp[i-1]
    dp[i] = (b,a+b)

print(str(dp[k][0]) + ' ' + str(dp[k][1]))