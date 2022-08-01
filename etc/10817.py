import sys
A,B,C = map(int,sys.stdin.readline().split())
if A > B:
    if B > C:
        print(B)
    else:
        if A > C:
            print(C)
        else:
            print(A)
else:
    if A > C:
        print(A)
    else:
        if B < C:
            print(B)
        else:
            print(C)


