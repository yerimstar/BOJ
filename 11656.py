word = input()
new = []
for i in range(len(word)):
    new.append(word[i:])
sort = sorted(new)
for i in range(len(new)):
    print(sort[i])