# 저울
import sys
n = int(sys.stdin.readline())
# 오름차순 정렬
lst = sorted(list(map(int,sys.stdin.readline().split())))

# 기준값
target = 1

for l in lst:
    if l > target:
        break
    else:
        target += l
print(target)
