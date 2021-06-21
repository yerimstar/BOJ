N = int(input())
num = list(range(10))
words = []
alpha = {}
tmp = {}

for i in range(N):
    word = input()
    words.append(word)
    for j in range(len(word)):
        alpha.append((len(word)-j,word[j],0))

for a in alpha:
    print(a[1])


alpha.sort(key=lambda x : (x[0],alpha.count(x[1])),reverse=True)
print(alpha)

for a in alpha:
    if a[1] in tmp: # 알파벳과 0~9 매칭
        continue
    else:
        tmp[a[1]] = str(max(num))
        num.remove(max(num))

result = 0
for i in range(N):
    tmpresult = ""
    for j in range(len(words[i])):
        tmpresult += tmp[words[i][j]]
    result += int(tmpresult)

print(result)
