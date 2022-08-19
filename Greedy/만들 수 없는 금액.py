import sys
n = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
lst.sort()
if lst[0] > 1:
    print(1)
    exit()
else:
    result = 1
for i in range(1,len(lst)):
    if result < lst[i]:
        print(result+1)
        exit()
    else:
        result += lst[i]

print(result+1)