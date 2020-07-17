N = int(input())
num = [0 for _ in range(N)]
for i in range(N//6):
    print("i = ", i)
    if i == 0:
        num[i] = 1
        x = 2
    else:
        for j in range(x,x+6*i):
            print("j = ", j)
            print("x+6*i",x+6*i)
            num[j] = i
            print(num[j])
            if j == (x+6*i-1):
                x = x + 6 * i

print(num[N])


