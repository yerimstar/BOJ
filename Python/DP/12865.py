# 평범한 배낭
import sys
def Knapsack(N,K,W,V):
    P = [[_ for _ in range(K+1)] for _ in range(N+1)]
    for i in range(N+1):
        for j in range(K+1):
            if i == 0 or j == 0:
                P[i][j] = 0
            elif W[i-1] <= j:
                P[i][j] = max(V[i-1] + P[i-1][j-W[i-1]],P[i-1][j])
            else:
                P[i][j] = P[i-1][j]
    return P[N][K]

N, K = map(int,sys.stdin.readline().split())
W = []
V = []
for _ in range(N):
    w,v = map(int,sys.stdin.readline().split())
    W.append(w)
    V.append(v)
print(Knapsack(N,K,W,V))
