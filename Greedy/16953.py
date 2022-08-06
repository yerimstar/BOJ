# A -> B
# 입력값
A,B = map(int,input().split())

# 횟수 측정
cnt = 1

while True:
    # B가 2로 나누어떨어진다면
    if B % 2 == 0:
        B //= 2
    # 일의 자리 값이 1이라면
    elif B % 10 == 1:
        B //= 10
    cnt += 1
    if A == B:
        break
    if B < A or (B % 2 != 0 and B % 10 != 1):
        cnt = -1
        break

print(cnt)







