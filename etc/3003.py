pieces = list(map(int,input().split()))
chess = [1,1,2,2,2,8]
i = 0
for piece in pieces:
    print(chess[i]-piece,end = ' ')
    i += 1