# 게임
import sys
def binary(start,end,win):
    while (start <= end):
        mid = (start + end) // 2 # 더 해야 하는 게임 횟수
        check = (((Y + mid) * 100) // (X + mid))
        if check > win:
            end = mid - 1
        else:
            start = mid + 1
        result = start
    return result

X,Y = map(int,sys.stdin.readline().split()) # X = 실행횟수 Y = 이긴횟수
start = 0
end = X
win = ((Y * 100)//X)
if win >= 99:
    print("-1")
else:
    result = binary(start,end,win)
    print(result)