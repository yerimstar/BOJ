# 두 용액
import sys

N = int(sys.stdin.readline().strip()) # 전체 용액의 수

solution = sorted(map(int,sys.stdin.readline().split())) # 용액

start = 0
end = N-1
final = list()
while start < end:
    mixture = [solution[start],solution[end],abs(solution[start] + solution[end])] # 혼합값
    final.append(mixture)
    sum = solution[start] + solution[end]
    if sum > 0: # 합이 양수이므로 큰 값을 줄여줘야 한다
        end = end -1
    elif sum < 0: # 합이 음수이므로 작은 값을 키워줘야 한다
        start = start + 1
    elif sum == 0: # 0인 경우 break
        break

final.sort(key=lambda x : x[2]) # 절댓값 기준으로 정렬한다.
print(final[0][0],final[0][1])
