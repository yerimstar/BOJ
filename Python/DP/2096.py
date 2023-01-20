# 내려가기
import sys

n = int(sys.stdin.readline())
min_dp = [[0 for _ in range(3)] for _ in range(2)]
max_dp = [[0 for _ in range(3)] for _ in range(2)]

for i in range(n):
    lst = list(map(int, sys.stdin.readline().split()))
    min_dp[1][0] = min(min_dp[0][0], min_dp[0][1]) + lst[0]
    max_dp[1][0] = max(max_dp[0][0], max_dp[0][1]) + lst[0]
    min_dp[1][1] = min(min_dp[0][0], min_dp[0][1], min_dp[0][2]) + lst[1]
    max_dp[1][1] = max(max_dp[0][0], max_dp[0][1], max_dp[0][2]) + lst[1]
    min_dp[1][2] = min(min_dp[0][1], min_dp[0][2]) + lst[2]
    max_dp[1][2] = max(max_dp[0][1], max_dp[0][2]) + lst[2]

    min_dp[0][0],min_dp[0][1],min_dp[0][2] = min_dp[1][0],min_dp[1][1],min_dp[1][2]
    max_dp[0][0], max_dp[0][1], max_dp[0][2] = max_dp[1][0], max_dp[1][1], max_dp[1][2]
print(max(max_dp[0]), min(min_dp[0]))
