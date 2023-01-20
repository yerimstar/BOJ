# 전화번호 목록
import sys

def fcheck(phone):
    for i in range(len(phone)-1):
        prefix = phone[i] # 접두어
        check = phone[i+1][:len(prefix)] # 접두어만 비교하기 위해 split
        if prefix == check: # 접두어가 동일한 경우 일관성이 없다고 판단
            print("NO")
            return
    print("YES")


T = int(sys.stdin.readline().rstrip()) # 테스트 케이스 개수
for _ in range(T):
    phone = list()
    N = int(sys.stdin.readline().rstrip()) # 전화번호 수
    for _ in range(N):
        phone.append((sys.stdin.readline().rstrip()))
    phone.sort() # 전화번호 정렬하기
    fcheck(phone)
