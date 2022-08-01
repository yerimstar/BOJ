# 보물
# B 리스트의 최댓값과 A의 최솟값을 순서대로 곱해주면 된다.
import sys

N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
B = list(map(int,sys.stdin.readline().split()))

S = 0
for _ in range(N):
    S += min(A) * max(B)
    A.pop(A.index(min(A)))
    B.pop(B.index(max(B)))
print(S)