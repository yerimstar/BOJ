import sys
N = int(sys.stdin.readline())
A = []
for i in range(N):
    data = list(map(int,sys.stdin.readline().split()))
    A.append(data)
A.sort(key = lambda x: (x[1],x[0]))
for a in A:
    print(a[0],a[1])