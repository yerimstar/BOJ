import collections

A = int(input())
B = int(input())
C = int(input())
multiply = A*B*C
count = collections.Counter(str(multiply))
for i in range(10):
    if count.get(str(i)):
        print(count.get(str(i)))
    else:
        print("0")