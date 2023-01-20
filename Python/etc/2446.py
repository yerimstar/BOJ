N = int(input())
for i in range(2*N-1):
    if i >= N:
        i = 2*(N-1)-i
    print(" "*i,"*"*(2*(N-i)-1),sep = '')
