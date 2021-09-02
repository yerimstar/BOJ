# 숫자 카드 2
import sys
N = int(sys.stdin.readline().rstrip())
card1 = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline().rstrip())
card2 = list(map(int,sys.stdin.readline().split()))

result = []
for card in card2:
    print(card)
    start = card1.index(card)
    end = len(card1)
    while(start <= end):
        count = 0
        mid = (start + end) // 2
        for c in card1:
            count +=