"""
# BOJ에서 Numpy 사용이 불가해서 수정함
M,N = map(int,input().split())
chess = []
for m in range(M):
    rows = []
    for n in range(N):
        rows.append(0)
    chess.append(rows)
black = (([1,0,1,0,1,0,1,0],[0,1,0,1,0,1,0,1])*4)
white = (([0,1,0,1,0,1,0,1],[1,0,1,0,1,0,1,0])*4)
for m in range(M):
    color = input()
    for n in range(N):
        if color[n] == "W":
            chess[m][n] = 0
        elif color[n] == "B":
            chess[m][n] = 1

final_count = []
for m in range(M - 8 + 1):
    for n in range(N - 8 + 1):
        count_b = 0
        count_w = 0
        for i in range(m,m+8):
            for j in range(n,n+8):
                if black[i-m][j-n] != chess[i][j]:
                    count_b += 1
                elif white[i-m][j-n] != chess[i][j]:
                    count_w += 1
        final_count.append(count_b)
        final_count.append(count_w)

print(min(final_count))
"""
import numpy as np
M,N = map(int,input().split())
chess = np.full((M,N),0)
black = np.array(([1,0,1,0,1,0,1,0],[0,1,0,1,0,1,0,1])*4)
white = np.array(([0,1,0,1,0,1,0,1],[1,0,1,0,1,0,1,0])*4)

for m in range(M):
    color = input()
    for n in range(N):
        if color[n] == "W":
            chess[m][n] = 0
        elif color[n] == "B":
            chess[m][n] = 1

final_count = []
for m in range(M - 8 + 1):
    for n in range(N - 8 + 1):
        count_b = 0
        count_w = 0
        for i in range(m,m+8):
            for j in range(n,n+8):
                if black[i-m][j-n] != chess[i][j]:
                    count_b += 1
                elif white[i-m][j-n] != chess[i][j]:
                    count_w += 1
        final_count.append(count_b)
        final_count.append(count_w)

print(min(final_count))

