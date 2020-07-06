test_num = int(input())
for i in range(test_num):
    H,W,N = map(int,input().split())
    X = N-H*(N//H)
    Y = (N//H)+1
    if X == 0:
        X = H
        Y = N//H
    print("%d%.02d"%(X,Y))