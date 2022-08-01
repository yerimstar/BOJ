import sys
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

tmp = []
T = int(sys.stdin.readline())
for i in range(0,T):
    N = int(sys.stdin.readline())
    t = fibonacci(N)
    check1 = N - t
    if N == 0:
        check1 += 1
    check2 = t
    print(str(check1) + " " + str(check2))
