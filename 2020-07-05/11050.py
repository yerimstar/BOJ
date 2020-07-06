"""
런타임 에러 뜸
N,K = map(int,input().split())
denominator = 1
numerator = 1
for i in range(N):
    denominator *= (N-i)
for i in range(K):
    numerator *= (K-i)*(N-K-i)
print(int(denominator/numerator))
"""