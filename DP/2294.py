# 동전 2
import sys
n,k = map(int,sys.stdin.readline().split())
coin = []
for _ in range(n):
    coin.append(int(sys.stdin.readline()))

dp = [10001] * (k+1)
dp[0] = 0
for i in range(n):
    for j in range(coin[i],k+1): # 자기 자신보다 작은 수는 만들 수 없음
        dp[j] = min(dp[j],dp[j-coin[i]]+1)
result = dp[-1]
if result == 10001:
    result = -1
print(result)