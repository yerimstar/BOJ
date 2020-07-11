import sys
N = int(sys.stdin.readline())
words = []
for i in range(N):
    words.append(sys.stdin.readline())
words.sort(key = len)

set_words = set(words)
print(set_words)



