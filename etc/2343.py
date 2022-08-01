# 기타 레슨
import sys
def binary(start,end,bluray,M):
    result = []
    while (start <= end):
        mid = (start + end) // 2
        num = 0
        sum = 0

        if mid < max(bluray):  # 최대 기타 강의 길이보다 mid값이 작은 경우 -> 담을 수 없음
            start = mid + 1
            continue

        for b in bluray:
            if sum + b <= mid:
                sum += b
            else:
                sum = b
                num += 1

        if num < M:
            result.append(mid)
            end = mid - 1
        else:
            start = mid + 1
    return result

N,M = map(int,sys.stdin.readline().split())
bluray = list(map(int,sys.stdin.readline().split()))
start = sum(bluray)//M
end = sum(bluray)
result = binary(start,end,bluray,M)
print(min(result))