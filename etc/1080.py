# 행렬
import sys
N,M = map(int,sys.stdin.readline().split())
A = [list(map(int,input())) for _ in range(N)]
B = [list(map(int,input()))for _ in range(N)]

if N < 3 or M < 3: # 3x3 행렬을 만들 수 없는 경우 -> -1 출력 (반례)
    if A == B:
        print(0)
    else:
        print(-1)
    exit()

count = 0
for i in range(N-2):
    for j in range(M-2):
        if A[i][j] != B[i][j]:
            count += 1
            for n in range(3):
                for m in range(3):
                    if A[i+n][j+m] == 0:
                        A[i+n][j+m] =1
                    elif A[i+n][j+m] == 1:
                        A[i + n][j + m] = 0
        if A == B:
            break

if A != B: # 3x3을 모두 시도해봐도 행렬이 다른 경우 -> -1 출력 (반례)
    print(-1)
else:
    print(count)