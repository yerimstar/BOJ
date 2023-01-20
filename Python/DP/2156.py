# 포도주 시식
import sys
n = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(n)]
dp = [0] * n

if n == 1:
    print(arr[0])
elif n == 2:
    print(arr[0]+arr[1])
else:
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]
    for i in range(2, n):
        dp[i] = max(dp[i - 3] + arr[i - 1] + arr[i], dp[i - 2] + arr[i],dp[i-1])
    print(dp[n-1])
