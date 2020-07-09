import sys
N = int(sys.stdin.readline())
B = []
C = []
A = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
B = list(map(int,sys.stdin.readline().split()))
for i in range(M):
    if B[i] in A:
        C.append(int("1"))
    else:
        C.append(int("0"))
for i in range(M):
    print(C[i])