# 전깃줄
import sys
n = int(sys.stdin.readline())
line = []
for _ in range(n):
    line.append(list(map(int,sys.stdin.readline().split())))

dp = [1] * (n+1)
line.sort(key = lambda x : x[0])
for i in range(1,n):
    for j in range(i):
        if line[j][1] < line[i][1]:
            dp[i] = max(dp[j]+1,dp[i])
print(n-max(dp))