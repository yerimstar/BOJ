N, K = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(N)]
S,X,Y = map(int,input().split())
move = [[-1,0],[1,0],[0,-1],[0,1]]
virus = [[(i,j)] for i in range(N) for j in range(N) for k in range(1,K+1) if lst[i][j] == k]

print(virus)
if S != 0:
    for s in range(S):
        for i in range(K):
            tmp = []
            for v in virus[i]:
                for m in move:
                    check1 = v[0] + m[0]
                    check2 = v[1] + m[1]
                    if (0 <= check1 < N) and (0 <= check2 < N):
                        if lst[check1][check2] == 0:
                            lst[check1][check2] = i + 1
                            tmp.append((check1, check2))
            virus[i] = tmp
print(lst)
print(virus)
print(lst[X-1][Y-1])