# 퇴사
import sys
n = int(sys.stdin.readline())

T = []
P = []
d = [0] * (n+1)
for i in range(n):
    t,p = map(int,sys.stdin.readline().split())
    T.append(t)
    P.append(p)

# 최댓값 비교
price_max = 0
for i in range(n):
    price_max = max(price_max,d[i])
    last = i + T[i] # 일이 끝나는 날 체크
    if last <= n: # 퇴사 날짜보다 해당 날짜가 작은 경우 -> 일할 수 있음
        d[last] = max(d[last],price_max+P[i])

print(max(d))