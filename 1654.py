# 랜선 자르기
import sys

K, N = list(map(int,sys.stdin.readline().rstrip().split()))
lan = [int(sys.stdin.readline().rstrip()) for x in range(K)]

start = 1
end = max(lan)

result = 0
while(start <= end):
    check = 0
    mid = (start + end) // 2
    for l in lan:
        check += (l // mid)
    if check < N:
        end = mid -1
    else:
        result = mid
        start = mid + 1
print(result)