# 문자열 폭발
import sys
s = sys.stdin.readline().strip()
bomb = sys.stdin.readline().strip()

tmp = []
for x in s:
    tmp.append(x)
    if bomb[-1] == x and ''.join(tmp[-1-len(bomb)+1:]) == bomb:
        del tmp[-1-len(bomb)+1:]
if tmp:
    print(''.join(tmp))
else:
    print("FRULA")