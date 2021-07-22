import sys
sys.setrecursionlimit(10**6)
N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int,input().rstrip())))

def dfs(x,y,check,result):
    if len(check) <= result:
        check.append(0)
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    if graph[x][y] == 1:
        graph[x][y] = check[result]
        check[result] += 1
        dfs(x-1,y,check,result)
        dfs(x+1,y,check,result)
        dfs(x,y-1,check,result)
        dfs(x,y+1,check,result)
        return True
    return False

result = 0
check = []
for i in range(N):
    for j in range(N):
        if dfs(i,j,check,result) == True:
            result += 1
print(result)
check = sorted(check[:-1])
for c in check:
    print(c-1)