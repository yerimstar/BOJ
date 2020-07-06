while(1):
    length = sorted(list(map(int,input().split())))
    if sum(length) == 0:
        break
    elif (length[0]**2)+ (length[1]**2) == (length[2]**2):
         print("right")
    else:
        print("wrong")