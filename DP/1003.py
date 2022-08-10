# 피보나치 함수
import sys

def fibo(n):
	# 테이블 갱신
    z[0] = 1
    z[1] = 0
    o[0] = 0
    o[1] = 1
	# DP 진행 - 보텀업 방식
    for i in range(2,n+1):
        z[i] = z[i-1]+z[i-2]
        o[i] = o[i-1]+o[i-2]

T = int(sys.stdin.readline())
for _ in range(T):
	# DP 테이블 생성 및 초기화
    z = [0] * 41
    o = [0] * 41
    n = int(sys.stdin.readline())
    fibo(n)
    print(z[n],o[n])