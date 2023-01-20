# 시험 감독
import sys
N = int(sys.stdin.readline())
classroom = list(map(int,sys.stdin.readline().split()))
B,C = map(int,sys.stdin.readline().split())

result = 0 # 전체 감독관 수
for cr in classroom:
    result += 1
    if cr - B > 0:
        if (cr-B) % C == 0:
            result +=  ((cr-B)//C)
        else:
            result += ((cr-B)//C + 1)
print(result)

