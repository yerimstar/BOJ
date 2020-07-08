import sys
def primenum(n):
    for i in range(2,n):
        if n%i == 0:
            return 0
            break
    return 1
N = int(sys.stdin.readline())
num = list(map(int,sys.stdin.readline().split()))
result = 0
for i in range(N):
    if num[i] == 1:
        pass
    else:
        result += primenum(num[i])
print(result)

