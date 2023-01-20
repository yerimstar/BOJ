import sys
n = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
lst.sort()

# 초기에 1을 더하고 시작한다
result = 1
for l in lst:
    if result < l:
        break
    result += l
print(result)