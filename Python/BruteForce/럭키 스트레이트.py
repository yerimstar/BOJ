import sys
lst = list(map(int,sys.stdin.readline().rstrip()))
check = len(lst) // 2
score1,score2 = 0,0
for i in range(len(lst)):
    if i < check:
        score1 += lst[i]
    else:
        score2 += lst[i]
print("LUCKY" if score1 == score2 else "READY")