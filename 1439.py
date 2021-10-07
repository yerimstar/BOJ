# 뒤집기
# 0101000 -> 최소 2번
S = list(input())

count_0 = 0
count_1 = 0

for i in range(len(S)): # 문자열을 순회하면서
    if i == 0:
        if S[i] == '0':
            count_0 += 1
        elif S[i] == '1':
            count_1 += 1
    else:
        if S[i] == '0':
            if S[i - 1] != S[i]:
                count_0 += 1
        elif S[i] == '1':
            if S[i - 1] != S[i]:
                count_1 += 1

print(min(count_0,count_1))


