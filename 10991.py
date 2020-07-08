N = int(input())
for i in range(1,N+1):
    if i%2 == 0:
        for k in range(1,2*i+1):
            if k%2 == 0:
                print(" ",end='')
            else:
                print("*",end='')
    else:
        for k in range(1,2*i+1):
            if k%2 == 0:
                print("*",end='')
            else:
                print(" ",end='')
    print()