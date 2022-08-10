# 피보나치 함수
import sys

def fibo(n):
    global zero_cnt,one_cnt
    if n == 0:
        zero_cnt += 1
        return 0
    elif n == 1:
        one_cnt += 1
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

T = int(sys.stdin.readline())
for _ in range(T):
    zero_cnt = 0
    one_cnt = 0
    n = int(sys.stdin.readline())
    fibo(n)
    print(zero_cnt,one_cnt)

