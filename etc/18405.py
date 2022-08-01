import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
lst = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
S,X,Y = map(int,input().split())

move = [[-1,0],[1,0],[0,-1],[0,1]]
virus = [[lst[i][j],i,j,0] for i in range(N) for j in range(N) if lst[i][j] != 0]

virus.sort() #lst[i][j] - 바이러스 값을 오름차순 정렬
virus = deque(virus)

while virus:
    v,i,j,t = virus.popleft() #바이러스 1번부터 값을 넣어두기
    if t == S:
        break
    else:
        for m in move:
            check1 = i + m[0]
            check2 = j + m[1]
            if (0 <= check1 < N) and (0 <= check2 < N) and (lst[check1][check2] == 0):
                lst[check1][check2] = v
                virus.append([v,check1,check2,t+1])
print(lst[X-1][Y-1])