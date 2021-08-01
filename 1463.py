# 1로 만들기
# DP
N = int(input()) # 정수 N입력
d = [0] * (10**6+1)

for i in range(2,N+1):
    d[i] = d[i-1]+1
    if i % 2 == 0:
        d[i] = min(d[i],d[i//2]+1)
    elif i % 3 == 0:
        d[i] = min(d[i],d[i//3]+1)
d[1] = 1
print(d[N])