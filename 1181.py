import sys
N = int(sys.stdin.readline())
words = []
for i in range(N):
    words.append(sys.stdin.readline().strip())
words.sort(key = len)
print(words)
new = []
for w in words:
    if w not in new:
        new.append(w)
print(new)





