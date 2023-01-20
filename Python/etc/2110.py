# 공유기 설치
import sys
N,C = list(map(int,sys.stdin.readline().split()))
home = [int(sys.stdin.readline().rstrip()) for x in range(N)]
home.sort()

# 거리의 최댓값을 구하는 문제 -> start,end도 거리값으로 지정
start = 1 # 거리 최소
end = home[-1] - home[0] # 거리 최대

result = 0
while(start <= end):
    check = 1
    mid = (start + end) // 2
    home_check = home[0]
    for h in home:
        print(h,home_check,mid)
        if h - home_check >= mid:
            check += 1
            home_check = h
            print(check)
    if check < C:
        end = mid - 1
    else:
        start = mid + 1
        result = mid
print(result)
