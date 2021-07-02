N = int(input())

def hanoi(n,start,final,middle):
    if n == 1:
        print(start,final)
    else:
        hanoi(n-1,start,middle,final)
        print(start,final)
        hanoi(n-1,middle,final,start)

print(2**N-1) # 계차수열
if N <= 20:
    hanoi(N,1,3,2)
