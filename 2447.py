def star(i,j):
    while(i!=0):
        if (i%3 == 1 & j%3 == 1):
            print(" ")
            return None
        i = i//3
        j = j//3
    print("*")


N = int(input())
for i in range(N):
    for j in range(N):
        star(i,j)
    print('\n')