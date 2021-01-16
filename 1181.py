from sys import stdin
words = list(set(stdin.readline().rstrip() for i in range(int(input()))))
new = []
for word in words:
    new.append((word,len(word)))
new.sort(key = lambda x:(x[1],x[0]))
for n in new:
    print(n[0])