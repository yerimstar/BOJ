# 단어 정렬하기
from queue import PriorityQueue

N = int(input())
que = PriorityQueue() # 우선순위 큐

for _ in range(N):
    que.put(int(input())) # 큐 데이터 삽입

result = 0
tmp = 0

for i in range(N-1):
    tmp = (que.get()+que.get()) # 큐 데이터 추출
    result += tmp # 결과값 저장
    que.put(tmp) # 데이터 2개를 더한 값을 우선순위 큐에 다시 넣어준다
print(result)