# 용돈 관리
import sys

def binary(start,end,money,M):
    result = end
    while(start <= end):
        mid = (start + end) // 2
        num = 0
        sum = 0

        if mid < max(money):
            start = mid + 1
            continue

        for m in money:
            if sum + m <= mid:
                sum += m
            else:
                sum = m
                num += 1
        if num < M:
            result = min(result,mid)
            end = mid - 1
        else:
            start = mid + 1
    return result

N,M = map(int,sys.stdin.readline().split())
money = [int(sys.stdin.readline()) for _ in range(N)]
start = sum(money)//M
end = sum(money)
result = binary(start,end,money,M)
print(result)