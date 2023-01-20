N = int(input())
if N == 1:
    print("*")
else:
    for k in range(N):
        print(" "*(N-k-1)+"* " * k+"*")