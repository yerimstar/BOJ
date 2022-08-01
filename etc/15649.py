def sequence(count):
    if count == M:
        for m in range(M):
            print(num[m],end = ' ')
        print()
    else:
        for i in range(1,N+1):
            print(isUsed[i])
            if (~isUsed[i]):
                num[count] = i
                isUsed[i] = True
                sequence(count+1)
                isUsed[i] = False

N,M = map(int,input().split())
isUsed = [False for _ in range(N+1)]
num = [0 for i in range(M)]
sequence(0)

