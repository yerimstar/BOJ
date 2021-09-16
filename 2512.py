# 예산
import sys
N = int(sys.stdin.readline().rstrip())
money = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline().rstrip())

if sum(money) < M: # 모든 요청이 배정될 수 있는 경우
    print(max(money))
else: # 모든 요청이 배정될 수 없는 경우 -> 이진 탐색
    start = 1
    end = max(money)
    result = 0
    while (start <= end):
        check = 0
        mid = (start + end) // 2 # 상한액 지정
        for m in money:
            if m <= mid: # 상한액 이하의 예산요청
                check += m
            else: # 상한액 배정
                check += mid
        if check > M: # 예산액 초과
            end = mid - 1
        else:
            result = mid
            start = mid + 1
    print(result)