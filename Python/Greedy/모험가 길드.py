import sys
n = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
lst.sort()
# 그룹 수
group = 0
# 현재 그룹에 있는 인원 수
cnt = 0
for l in lst:
    # 현재 그룹에 인원 추가
    cnt += 1
    # 현재 그룹에 있는 인원수가 현재 비교하고자 하는 공포도보다 크거나 같을 경우
    # 그룹을 형성할 수 있음
    if cnt >= l:
        # 그룹 형성
        group += 1
        # 새로운 그룹을 만들어야 하므로 그룹 인원 초기화
        cnt = 0
print(group)