import sys
N,M = map(int,sys.stdin.readline().split())
L = [input() for _ in range(N)] # 듣도 못한 사람들
S = [input() for _ in range(M)] # 보도 못한 사람들
result = sorted(list(set(L) & set(S)))
print(len(result))
print(*result,sep='\n')
