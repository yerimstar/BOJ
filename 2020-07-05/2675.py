T = int(input())
for i in range(T):
    R,S = input().split()
    P = '' #P는 문자열
    for i in S:
        P += int(R) * i
    print(P)