# 영역 구하기
# 1차 아이디어
"""
K개 직사각형 내부의 값들을 1로 처리, 나머지 값들은 0으로 처리
음료수 얼려 먹기..문제처럼 푼다.-> dfs (재귀)
다만, count를 큰 범위, 작은 범위 2번 check
"""
import sys
sys.setrecursionlimit(10**6) # 파이싼 기본 재귀 깊이 제한 = 1000이기 때문에 제한에 걸림 !!
M,N,K = map(int,sys.stdin.readline().split())
graph = [[0] * (N+1) for _ in range(M+1)]

def dfs(x,y,check,result):
    if len(check) <= result:
        check.append(0) # 각 영역의 넓이 저장
    if x < 0 or x >= M or y < 0 or y >= N:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        check[result] += 1
        dfs(x-1,y,check,result)
        dfs(x+1,y,check,result)
        dfs(x,y-1,check,result)
        dfs(x,y+1,check,result)
        return True
    return False

for i in range(K):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
    for x in range(M-y2,M-y1):
        for y in range(x1,x2):
            graph[x][y] = 1

result = 0
check = []
for i in range(M):
    for j in range(N):
        if dfs(i,j,check,result) == True:
            result += 1

print(result)
print(' '.join(map(str,sorted(check[:result])))) # int형 리스트 출력시 map으로 str변환 해줘야 함