# 계단 오르기
import sys
# 계단 개수
n = int(sys.stdin.readline())
# 계단 점수
score = [0,]
for _ in range(n):
    score.append(int(sys.stdin.readline()))

d = [0] * (n+1)
d[1] = score[1]
d[2] = d[1] + score[2]

for i in range(3,n+1):
    d[i] = max(d[i-2],d[i-3]+score[i-1])+score[i]
print(d[n])

