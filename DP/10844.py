#  쉬운 계단수
import sys
n = int(sys.stdin.readline())

# dp[자리수][0~9 숫자]
dp = [[1 for _ in range(10)] for _ in range(n)]
dp[0][0] = 0 # 맨 앞에 0이 올 수 없음

for i in range(1,n):
    dp[i][0] = dp[i-1][1]
    dp[i][9] = dp[i-1][8]
    for j in range(1,9):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
result = 0
for i in range(10):
    result += dp[n-1][i]
print(result%(10**9))
