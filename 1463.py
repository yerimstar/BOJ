# 1로 만들기
# DP
N = int(input()) # 정수 N입력
d = [0,0,1,1]

for i in range(4,N+1):
    d.append(d[i-1]+1) # 1을 뺄 경우 1을 만든다.
    if i % 2 == 0:
        d[i] = min(d[i],d[i//2]+1) # 2로 나누어 떨어진다
    if i % 3 == 0:
        d[i] = min(d[i],d[i//3]+1) # 3으로 나누어 떨어진다.
print(d[N])
