# 플로이드
import sys

INF = int(1e9) # 무한대 값 지정

# 도시의 개수, 버스의 개수 입력받기
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[INF] * (n+1) for _ in range(n+1)]

# 각 버스의 필요 비용 입력
for _ in range(m):
    # a는 시작 도시, b는 도착 도시, c는 필요비용
    a,b,c = map(int,sys.stdin.readline().split())
    # 노선이 여러개일 수 있기 때문에 최솟값 비교 과정이 필요하다
    graph[a][b] = min(graph[a][b],c)

# 시작과 도착이 똑같은 경우 0값으로 초기화
# 도시값의 범위가 1 <= n <= 100이므로 1~n+1에 값을 저장해야 한다.
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:
            graph[i][j] = 0

# 최단 경로 업데이트 -> 점화식을 활용한 플로이드 워셜 알고리즘
# i -> j 경로와 i -> k + k -> j 중 최솟값이 최단 경로 값이 됨
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j],graph[i][k] + graph[k][j])

# 출력
for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == INF:
            print(0, end = " ")
        else:
            print(graph[i][j], end = " ")
    print()
