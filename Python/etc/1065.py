import sys
num = int(sys.stdin.readline())
count = 0
for i in range(1,num+1):
    if i <= 99:
        count += 1
    else:
        a = i//100
        b = (i-a*100)//10
        c = i-a*100-b*10
        if (c-b)==(b-a):
            count += 1
print(count)
