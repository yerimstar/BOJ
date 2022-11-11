# 문자열 폭발
import sys
s = sys.stdin.readline().strip()
bomb = sys.stdin.readline().strip()
while bomb in s:
    s = s.replace(bomb,'')
if s:
    print(s)
else:
    print("FRULA")