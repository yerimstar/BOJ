import sys
L = int(sys.stdin.readline())
str = sys.stdin.readline()
sum = 0
for i in range(0,L):
    sum += (ord(str[i])-96)*(31**i)
print(sum%1234567891)
