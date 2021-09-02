# 입국심사
import sys
N,M = list(map(int,sys.stdin.readline().split()))
delay = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

start = 1
end = M * max(delay) # 오래 걸리는 심사관한테 계속 심사받는 경우

result = 0
while(start <= end):
    check = 0
    mid = (start + end) // 2
    for d in delay:
        check += mid // d
    if check < M:
        start = mid + 1
    else:
        end = mid - 1
        result = mid
print(result)