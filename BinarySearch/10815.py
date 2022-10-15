# 숫자 카드
import sys

def BinarySearch(s):
    left = 0
    right = M-1
    while left <= right:
        mid = (left+right)//2
        if sang[mid] == s:
            lst.append(1)
            break
        elif sang[mid] > s:
            right = mid - 1
        elif sang[mid] < s:
            left = mid + 1
    lst.append(0)

N = int(sys.stdin.readline().strip())
sang = list(map(int,sys.stdin.readline().split()))
sang.sort()
M = int(sys.stdin.readline().strip())
check = list(map(int,sys.stdin.readline().split()))
lst = []

for c in check:
    BinarySearch(c)
print(' '.join(map(str,lst)))