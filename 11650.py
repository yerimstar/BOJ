"""
시간초과
import sys
N = int(sys.stdin.readline())
A = []
for i in range(N):
    x,y = map(int,sys.stdin.readline().split())
    A.append([x,y])
for i in range(N):
    for k in range(N):
        if A[i][0] < A[k][0]:
            temp = A[i]
            A[i]=A[k]
            A[k] = temp
        elif A[i][0] == A[k][0]:
            if A[i][1] < A[k][1]:
                temp = A[i]
                A[i] = A[k]
                A[k] = temp
for i in range(N):
    print(A[i])
"""
import sys
N = int(sys.stdin.readline())
A = []
for i in range(N):
    data = list(map(int,sys.stdin.readline().split()))
    A.append(data)
A.sort(key = lambda x: (x[0],x[1]))
for a in A:
    print(a[0],a[1])