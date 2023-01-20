import sys
# 문자열 -> int
lst = list(map(int,list(sys.stdin.readline().rstrip())))
answer = 0
for l in lst:
    # 숫자 값은 0~9라고 명시되어 있기 때문에 음수가 나올 확률은 없음
    # 최댓값을 만드는 문제이기 때문에 더하기보다 곱하기 연산이 이득이다.
    # 0 또는 1은 곱하기보다 더하기가 더 큰 값을 만들기 때문에 이 부분은 예외처리해줘야 한다
    # 새로 연산하는 값과 결과값을 함께 검사해줘야 한다.
    if l <= 1 or answer <= 1:
        answer += l
    else:
        answer *= l
print(answer)