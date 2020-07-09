"""
1번 시도 - 시간 초과
import sys
N = int(sys.stdin.readline())
N_list = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_list = list(map(int,sys.stdin.readline().split()))
result = []
for m in M_list:
    result.append(N_list.count(m))
for r in result:
    print(r,end=' ')

2번 시도 - 시간 초과
import sys
N = int(sys.stdin.readline())
N_list = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_list = list(map(int,sys.stdin.readline().split()))
for m in M_list:
    print(N_list.count(m),end = ' ')
=> list의 count가 시간을 많이 쓰는 듯..이 부분을 해결해야됨
"""
