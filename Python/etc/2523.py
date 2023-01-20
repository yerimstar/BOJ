N = int(input())
for i in range(2*N-1):
    if i < N:
        print("*"*(i+1))
    else:
        print("*"*(2*N-1-i))