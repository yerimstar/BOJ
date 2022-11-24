# 연속 부분 최대 곱
import sys
n = int(sys.stdin.readline())
lst = []
dp = [0] * (n+1)
for _ in range(n):
    lst.append(float(sys.stdin.readline().strip()))
dp[0] = lst[0]
for i in range(1,n):
    dp[i] = max(dp[i-1]*lst[i],lst[i])
print(round(max(dp),3))