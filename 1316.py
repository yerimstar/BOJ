from string import ascii_lowercase
import sys
alphabet = list(ascii_lowercase)
N = int(sys.stdin.readline())
group = 0
for i in range(N):
    word = sys.stdin.readline().strip('\n')
    check = []
    for k in range(len(word)):
        if word[k] in check:
            if word[k] == word[k-1]:
                if k == (len(word) - 1):
                    group += 1
                pass
            else:
                break
        elif word[k] not in check:
            check.append(word[k])
            if k == (len(word)-1):
                group+=1
print(group)