import sys
x = sys.stdin.readline().rstrip()
answer = ''
number = 0
for s in x:
    if s.isalpha():
        answer += s
    else:
        number += int(s)

answer = ''.join(sorted(answer))
answer += str(number)
print(answer)