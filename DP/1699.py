# 제곱수의 합
import sys
n = int(sys.stdin.readline())
dp = [i for i in range(n+1)]
for i in range(n+1):
    for j in range(1,i):
        if j**2 > i:
            break
        if dp[i] > dp[i-j**2] + 1:
            dp[i] = dp[i-j**2] + 1
print(dp[n])