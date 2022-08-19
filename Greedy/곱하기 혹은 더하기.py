import sys
lst = list(map(int,list(sys.stdin.readline().rstrip())))
answer = 0
for l in lst:
    if l <= 1 or answer <= 1:
        answer += l
    else:
        answer *= l
print(answer)