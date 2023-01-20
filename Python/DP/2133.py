# 타일 채우기
import sys
n = int(sys.stdin.readline())
dp = [0 for _ in range(n+1)]
if n >= 2:
    dp[2] = 3
for i in range(4,n+1,2):
    dp[i] = dp[i-2] * 3
    for j in range(0,i-2,2):
        dp[i] += dp[j] * 2
    dp[i] += 2
print(dp[n])
'''
dp
0 0 3 0 11 0 41 ...
'''