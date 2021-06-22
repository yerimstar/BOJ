N = int(input())
num = list(range(10))
words = []
tmp = {}
new = {}

for _ in range(N):
    words.append(input())

for word in words:
    for i in range(len(word)):
        if word[i] in tmp:
            tmp[word[i]] += (10**(len(word)-i-1))
        else:
            tmp[word[i]] = (10**(len(word)-i-1))

tmp = sorted(tmp.items(), key = lambda x : x[1], reverse= True)

num = 9
for i in range(len(tmp)):
    new[tmp[i][0]] = num
    num -= 1

result = 0
for word in words:
    tmpresult = ""
    for w in word:
        tmpresult += str(new[w])
    result += int(tmpresult)
print(result)
