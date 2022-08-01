import sys
Num = int(sys.stdin.readline())
check = 0
N = Num
while(1):
    M = (N//10)+(N%10)
    N = (N%10)*10+(M%10)
    check +=1
    if N == Num:
        break
print(check)