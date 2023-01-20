import sys
import math
sum_prime = []
def isPrime(num):
    if num == 1:
        return False
    for i in range(2,int(math.sqrt(num))+1):
        if num%i == 0:
            return False
    return True
M = int(sys.stdin.readline())
N = int(sys.stdin.readline())
for i in range(M,N+1):
    if isPrime(i):
        sum_prime.append(i)
if len(sum_prime)==0:
    print("-1")
else:
    print(sum(sum_prime))
    print(min(sum_prime))
