# 연속 부분 최대 곱
import sys
n = int(sys.stdin.readline())
dp = []
for _ in range(n):
    dp.append(float(sys.stdin.readline().strip()))
for i in range(1,n):
    dp[i] = max(dp[i-1]*dp[i],dp[i])
print('%.3f' %(max(dp)))