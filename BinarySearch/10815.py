# 숫자 카드
import sys

def BinarySearch(s):
    left = 0
    right = N-1
    while left <= right:
        mid = (left+right)//2
        if card[mid] == s:
            lst.append(1)
            return
        elif card[mid] > s:
            right = mid - 1
        elif card[mid] < s:
            left = mid + 1
    lst.append(0)

N = int(sys.stdin.readline().strip())
card = list(map(int,sys.stdin.readline().split()))
card.sort()
M = int(sys.stdin.readline().strip())
check = list(map(int,sys.stdin.readline().split()))
lst = []

for c in check:
    BinarySearch(c)
print(' '.join(map(str,lst)))