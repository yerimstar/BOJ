T = int(input())
for i in range(T):
    x,y = map(int,input().split())
    count = 2
    temp = [0,1,2]
    length = 0
    while(1):

        if length == (y-x):
            print(count)
