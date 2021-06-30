N, M = map(int,input().split())

if N == 1 or M == 1:
    print(1)
elif N == 2:
    if M < 3:
        print(1)
    elif 3 <= M < 5:
        print(2)
    elif 5 <= M < 7:
        print(3)
    else:
        print(4)
elif N >= 3:
    if M < 4:
        print(M)
    elif 4 <= M < 7:
        print(4)
    else:
        print(M-2)
