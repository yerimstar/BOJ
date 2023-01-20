# 이동하기
import sys
n,m = map(int,sys.stdin.readline().split())
lst = []
dp = [[0 for _ in range(m)] for _ in range(n)]
for _ in range(n):
    lst.append(list(map(int,sys.stdin.readline().split())))
dp[0][0] = lst[0][0]

for i in range(n):
    for j in range(m):
        for dx,dy in ((i-1,j),(i,j-1),(i-1,j-1)):
            if 0 <= dx < n and 0 <= dy < m:
                dp[i][j] = max(dp[dx][dy] + lst[i][j],dp[i][j])
print(dp[n-1][m-1])
'''
(1,1) -> (N,M)
(r+1,c),(r,c+1),(r+1,c+1) 이동 가능
-> 사탕 가져갈 수 있음
'''