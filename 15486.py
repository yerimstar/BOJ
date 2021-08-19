# 퇴사 2
# 계단 문제와 유사함
import sys
N = int(sys.stdin.readline())
T = [0] * (N)
P = [0] * (N)
sums = [0] * (1500002)

for i in range(N):
    T[i],P[i] = map(int,sys.stdin.readline().rstrip().split())

for i in range(N-1,-1,-1):
    if i + T[i] <= N:
        sums[i] = max(P[i]+sums[i+T[i]],sums[i+1])
    else:
        if i == N-1:
            sums[i] = 0
        else:
            sums[i] = sums[i+1]

print(max(sums))
