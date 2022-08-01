# N-Queen
import sys
def promising(i,col):
    k = 1
    while k < i:
        # 같은 열에 있거나 대각선에 있는지 검사
        if (col[i] == col[k] or abs(col[i] - col[k]) == (i-k)):
            return False
        k += 1
    return True

def n_queens(i,col):
    global result
    n = len(col) - 1 # depth
    if promising(i,col):
        if i == n:
            result += 1
        else:
            for j in range(1,n+1):
                col[i+1] = j
                n_queens(i+1,col)

N = int(sys.stdin.readline().strip())
col = [0] * (N+1)
result = 0
n_queens(0,col)
print(result)
