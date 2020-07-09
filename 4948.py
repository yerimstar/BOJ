#1번 시도 - 시간 초과 -> PyPy3로 돌리니깐 시간 문제 해결됨
import sys
import math
def isPrime(num):
    if num == 1:
        return 0
    for i in range(2,int(math.sqrt(num))+1):
        if num%i == 0:
            return 0
    return 1
while(1):
    N = int(sys.stdin.readline())
    count = 0
    if N == 0:
        break
    for i in range(N+1,2*N+1):
        count += isPrime(i)
    print(count)
