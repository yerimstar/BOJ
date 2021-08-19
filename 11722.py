# 가장 긴 감소하는 부분 수열
# 구글링함...값을 저장해준다는게 핵심..!
# 조건에서 수열이라는 것을 명시해줌!
import sys
N = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
length = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if arr[j] > arr[i]:
            length[i] = max(length[i],length[j]+1)

print(max(length))