import sys
N = int(sys.stdin.readline())
if N == 1:
    print("*")
else:
    for i in range(N):
        if N % 2 == 0:
            M = N//2
            print("* "*M)
            print(" *" *M)
        else:
            M = N//2+1
            print("* "*M)
            print(" "+"* "*(M-1))