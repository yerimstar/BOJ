import sys
n,m = map(int,sys.stdin.readline().split())
lst = list(map(int,sys.stdin.readline().split()))
dp = [0 for _ in range(n)]
dp[0] = lst[0]
for i in range(n):
    dp[i] = dp[i-1] + lst[i]
for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    print(dp[b-1]-dp[a-1]+lst[a-1])
