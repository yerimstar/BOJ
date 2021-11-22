# 전화번호 목록
import sys

T = int(sys.stdin.readline().rstrip()) # 테스트 케이스 개수
for _ in range(T):
    phone = list()
    N = int(sys.stdin.readline().rstrip()) # 전화번호 수
    for _ in range(N):
        phone.append(sys.stdin.readline().rstrip())
    phone.sort()
    check = 0
    for p in phone:
        for x in phone:
            if p in x and p != x:
                print("NO")
                check += 1
                break
    if check == 0:
        print("YES")