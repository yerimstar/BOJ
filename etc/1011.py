T = int(input())
for i in range(T):
    x,y = map(int,input().split())
    length = y-x
    num = 1
    while(1):
        if num**2 <= length < (num+1)**2:
            break
        num += 1
    if num**2 == length:
        print((num*2)-1)
    elif num**2 < length <= (num**2)+num:
        print(num*2)
    else:
        print((num*2)+1)