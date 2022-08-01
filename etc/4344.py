import sys
C = int(sys.stdin.readline())
for i in range(C):
    N = list(map(int,sys.stdin.readline().split()))
    sum = 0
    count = 0
    for k in range(N[0]):
        sum += N[k+1]
    for k in range(N[0]):
        if (sum/N[0]) < N[k+1]:
            count += 1
    print("%.3f%%" %((count/N[0])*100))
