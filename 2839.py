import sys
N = int(sys.stdin.readline())
box = []
X = N//3
for i in range(X+1):
    for j in range(X+1):
        a = i*3+5*j
        if N == a:
            box.append(i+j)
if len(box)==0:
    print("-1")
else:
    print(min(box))


