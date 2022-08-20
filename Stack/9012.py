# 괄호
import sys
t = int(sys.stdin.readline())
for _ in range(t):
    answer = 'YES'
    # 문자열 입력
    checkstr = sys.stdin.readline().rstrip()
    # 스택 선언
    stack = []
    for s in checkstr:
        if s == '(':
            stack.append('(')
        elif s == ')':
            if len(stack) != 0:
                stack.pop()
            else:
                answer = 'NO'
    if len(stack) != 0:
        answer = 'NO'
    print(answer)