# A -> B
# 입력값
A,B = map(int,input().split())

# 횟수 측정
cnt = 0

while True:
    if A == B:
        print(cnt+1)
        break
    # B가 2로 나누어떨어진다면
    if B % 2 == 0:
        B //= 2
        cnt += 1 # 횟수 증가
    else:
        # 일의 자리 값이 1이라면
        if str(B)[-1] == "1":
            B = int(str(B)[:-1])
            cnt += 1
    if B < A:
        print(-1)
        break








