# 숫자 카드 2
import sys
N = int(sys.stdin.readline().rstrip())
card1 = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline().rstrip())
card2 = list(map(int,sys.stdin.readline().split()))

counts = dict()
for card in card1:
    if card in counts:
        counts[card] += 1
    else:
        counts[card] = 1

for card in card2:
    if card in counts:
        print(counts[card],end = ' ')
    else:
        print(0,end = ' ')