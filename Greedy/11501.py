# 주식
# 테스트케이스
import sys
T = int(sys.stdin.readline())

result = []
for _ in range(T):
    # 결과
    tmpResult = 0
    # 날의 수
    N = int(sys.stdin.readline())
    # 주가
    stock = list(map(int, sys.stdin.readline().split()))

    # 주가 최댓값 지정
    max_price = stock[-1]
    # 뒤에서부터 순회하면서 값 비교
    for i in range(N - 2, -1, -1):
        # 현재 결정된 주가 최댓값보다 값이 작다면 차이를 계산한다. 차이 == 이익
        if max_price >= stock[i]:
            tmpResult += (max_price - stock[i])
        # 현재 결정된 주가 최댓값보다 값이 크다면 주가 최댓값을 변경한다.
        else:
            max_price = stock[i]
    result.append(tmpResult)

for r in result:
    print(r)
