import sys
N = int(sys.stdin.readline())
result = 1
for i in range(N):
    result *= (N-i)
print(result)