"""
1번 시도
시간초과
import sys
nums = []
M,N = map(int,sys.stdin.readline().split())
for i in range(M,N+1):
    for k in range(2,i):
        if i%k == 0:
            break
        if k == (i-1):
            nums.append(i)
for num in nums:
    print(num)

2번 시도
시간초과
import sys
M,N = map(int,sys.stdin.readline().split())
for i in range(M,N+1):
    for k in range(2,i):
        if i%k == 0:
            break
        if k == (i-1):
            print(i)
"""
import sys
import math
def isPrime(num):
    if num == 1:
        return False
    for i in range(2,int(math.sqrt(num))+1):
        if num%i == 0:
            return False
    return True
M,N = map(int,sys.stdin.readline().split())
for i in range(M,N+1):
    if isPrime(i):
        print(i)