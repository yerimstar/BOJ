# 수리공 항승
import sys
# N - 물이 새는 곳의 개수, L - 테이프 길이
N,L = map(int,sys.stdin.readline().split())
# 물이 새는 곳의 위치
spot = list(map(int,sys.stdin.readline().split()))
spot = sorted(spot)

# 테이프 개수
tapeCnt = 1
check = 0
for i in range(1,N):
    # L-1 = 테이프 길이 - 0.5*2
    if abs(spot[i]-spot[check]) > L-1:
        tapeCnt += 1
        check = i
print(tapeCnt)