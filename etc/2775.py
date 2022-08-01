N = int(input())
def room(k,n):
    sum = 0
    if k == 0:
        return n
    else:
        for j in range(1,n+1):
            sum += room(k-1,j)
    return sum

for i in range(N):
    k = int(input())
    n = int(input())
    print(room(k,n))