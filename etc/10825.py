# 국영수
import sys

n = int(sys.stdin.readline().strip())
score = []
for _ in range(n):
    tmp = sys.stdin.readline().split()
    tmp[1] = int(tmp[1])
    tmp[2] = int(tmp[2])
    tmp[3] = int(tmp[3])
    score.append(tmp)
score.sort(key = lambda x: (-x[1],x[2],-x[3],x[0]))
for i in range(n):
    print(score[i][0])