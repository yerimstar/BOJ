# 공유기 설치
import sys
n,c = map(int,sys.stdin.readline().split())
house = []

# 집의 좌표 값 입력받기
for _ in range(n):
    xi = int(sys.stdin.readline().rstrip())
    house.append(xi)

# 집의 좌표 값 정렬하기
house.sort()

# 이분 탐색
def binary_search(house):
    start = 1 # 최소 거리
    end = house[-1] - house[0] # 최대 거리
    result = 0

    while start <= end:
        cnt = 1  # 공유기 수
        mid = (start + end) // 2
        now = house[0] # 현재 위치 (공유기 설치)
        # 공유기 사이 거리 측정
        for i in range(1,len(house)):
            if now + mid <= house[i]:
                cnt += 1 # 공유기 수 증가
                now = house[i] # 위치 변경 (공유기 설치)
        # 공유가 수가 충분함 -> 간격 늘리기
        if c <= cnt:
            start = mid + 1
            result = mid
        # 공유기 수가 부족한 경우 -> 간격을 좁힌다.
        else:
            end = mid - 1

    print(result)

binary_search(house)



