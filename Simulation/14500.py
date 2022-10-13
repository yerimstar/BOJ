# 테트로미노
import sys
tetromino = [[[0,0],[0,1],[0,2],[0,3]],[[0,0],[1,0],[2,0],[3,0]],
             [[0,0],[0,1],[1,0],[1,1]],
             [[0,0],[1,0],[2,0],[2,1]],[[0,0],[0,1],[0,2],[1,0]],[[0,0],[0,1],[1,1],[2,1]],[[1,0],[1,1],[1,2],[0,2]],
             [[0,1],[1,1],[2,1],[0,2]],[[0,0],[1,0],[1,1],[1,2]],[[0,0],[0,1],[1,0],[2,0]],[[0,0],[0,1],[0,2],[2,1]],
             [[0,0],[0,1],[0,2],[1,1]],[[0,1],[1,1],[2,1],[1,1]],[[1,0],[1,1],[1,2],[0,1]],[[0,0],[1,0],[2,0],[1,1]],
             [[0,0],[1,0],[1,1],[2,1]],[[1,0],[1,1],[0,1],[0,2]],[[0,1],[1,0],[1,1],[2,0]],[[0,0],[0,1],[1,1],[1,2]]]
N,M = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(map(int,sys.stdin.readline().split())))
result  = 0
for i in range(N):
    for j in range(M):
        for t in tetromino:
            tmp = 0
            for k in range(4):
                dx = i + t[k][0]
                dy = j + t[k][1]
                if 0 <= dx < N and 0 <= dy < M:
                    tmp += graph[dx][dy]
                else:
                    tmp = 0
                    break
            result = max(result,tmp)
print(result)