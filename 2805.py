# 나무 자르기
import sys

N,M = list(map(int,sys.stdin.readline().rstrip().split()))
tree = list(map(int,sys.stdin.readline().rstrip().split()))

start = 0
end = max(tree)

result = 0
while(start <= end):
    check = 0
    mid = (start + end) // 2
    for t in tree:
        if t - mid > 0:
            check += (t - mid)
    if check < M: # 왼쪽 부분 탐색
        end = mid - 1
    else: # 오른쪽 부분 탐색
        result = mid
        start = mid + 1

print(result)