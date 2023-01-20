# 팰린드롬수
import sys
while True:
    n = sys.stdin.readline().strip()
    if int(n) == 0:
        break

    l = len(n)
    num = n[::-1]


    if l % 2 == 0:
        if num[l//2:] == n[l // 2:]:
            print("yes")
        else:
            print("no")
    else:
        if num[l//2+1:] == n[l // 2 + 1:]:
            print("yes")
        else:
            print("no")

