"""
# 시간초과
def isPrime(n):
    if n!= 1:
        for i in range(2,n):
            if n % i == 0:
                return False
    else:
        return False

    return True

T = int(input())
for i in range(T):
    Prime = []
    N = int(input())
    for j in range(2,N):
        if isPrime(j):
            a = j
            for k in range(2, N):
                if isPrime(k):
                    b = k
                    if N == (a + b):
                        Prime.append((a, b))
    for p in range(len(Prime)):
        min_prime = abs(Prime[p][0]-Prime[p][1])
        if p == 0:
            min = min_prime
        elif min > min_prime:
            min = min_prime
    for p in range(len(Prime)):
        if min == abs(Prime[p][0]-Prime[p][1]):
            print(Prime[p][0],Prime[p][1])
            break
"""
def isPrime(n):
    a = [False,False] + [True]*(n-1)
    primes = []
    for i in range(2,n+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i,n+1,i):
                a[j] = False
    Prime = [(i,j) for i in primes for j in primes if i+j == n]
    Diff = [abs(p[0]-p[1]) for p in Prime]
    return Prime,Diff

for _ in range(int(input())):
    N = int(input())
    Prime,Diff = isPrime(N)
    for p in range(len(Prime)):
        if  min(Diff) == abs(Prime[p][0]-Prime[p][1]):
            print(Prime[p][0],Prime[p][1])
            break