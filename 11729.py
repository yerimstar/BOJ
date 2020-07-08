import sys
def hanoi(N,start,temp,end):
    if N == 1:
        print(start,end)
    else:
        hanoi(N-1,start,end,temp)
        hanoi(1,start,temp,end)
        hanoi(N-1,temp,start,end)
N = int(sys.stdin.readline())
print(2**N-1)
hanoi(N,1,2,3)
