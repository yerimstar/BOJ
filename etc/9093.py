import sys
N = int(sys.stdin.readline())
for i in range(N):
    sentence = list(sys.stdin.readline().split())
    for word in sentence:
        new = list(word)
        new.reverse()
        word = "".join(new)
        print(word,end=' ')
    print()