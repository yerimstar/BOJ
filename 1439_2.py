# 뒤집기
import sys

S = list(map(int,list(sys.stdin.readline().strip())))

# 구간별 횟수 측정
one_to_zero = 0
zero_to_one = 0

if S[0] == 0:
    one_to_zero += 1
elif S[0] == 1:
    zero_to_one += 1

check = S[0]
for i in range(1,len(S)):
    if check != S[i]:
        if S[i] == 0:
            one_to_zero += 1
        elif S[i] == 1:
            zero_to_one += 1
    check = S[i]

print(min(one_to_zero,zero_to_one))


