# 동물원
import sys
n = int(sys.stdin.readline())
# dp[i][0] 아무것도 선택 x, dp[i][1] 왼쪽 칸 선택, dp[i][2] 오른쪽 칸 선택
dp = [[0,0,0] for _ in range(n)]
dp[0][0] = 1 # 한 마리도 배치하지 않는 경우도 하나의 경우의 수
dp[0][1] = 1
dp[0][2] = 1
for i in range(1,n):
    dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % 9901
    dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % 9901
    dp[i][2] = (dp[i-1][0] + dp[i-1][1]) % 9901
print(sum(dp[n-1])%9901)
