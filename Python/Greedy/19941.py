# 햄버거 분배
import sys
N, K = map(int,sys.stdin.readline().split())
# rstrip() - 개행 제거
lst = list(sys.stdin.readline().rstrip())
result = 0
# lst을 돌면서 사람이 있으면 햄버거를 먹을 수 있는지 판단한다.
for i in range(N):
    # 사람 발견
    if lst[i] == 'P':
        # 검사 범위 조정
        if i-K < 0:
            start = 0
        else:
            start = i-K

        if i+K >= N:
            end = N
        else:
            end = i+K+1

        # 남아있는 햄버거 찾기
        for j in range(start,end): # K는 최대 10
            if lst[j] == 'H':
                # 햄버거를 먹은 경우 사람과 햄버거 모두 0값으로 치환해준다
                lst[i] = 0
                lst[j] = 0
                result += 1
                break
print(result)



