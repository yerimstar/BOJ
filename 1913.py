N = int(input()) # NxN
M = int(input()) # M의 위치는?
array = [[0 for col in range(N)] for row in range(N)]
num = int((N-1)/2)
array[num][num] = 1
check1 = num
check2 = num # check는 현재 위치

lst_move = [[-1,0],[1,0],[0,-1],[-1,0]] #인덱스 방향 전환
lst = [[0,1],[1,0],[0,-1],[-1,0]] #값이 이동하는 방향

tmp = 1
for i in range(1,num+1):
    for j in range(4):
        check1 += lst_move[j][0]
        check2 += lst_move[j][1]
        for k in range(i*2):
            tmp += 1
            array[check1+k*lst[j][0]][check2+k*lst[j][1]] = tmp
            if k == (i*2-1):
                check1 = check1+k*lst[j][0]
                check2 = check2+k*lst[j][1]

for arr in array:
    print(' '.join(str(a) for a in arr))

for i in range(N):
    if M in array[i]:
        print(i+1,array[i].index(M)+1)
        exit()

