# 단어 수학
N = int(input())
num = list(range(10))
words = []
tmp = {}
new = {}

for _ in range(N):
    words.append(input())

for word in words: # 각 알파벳의 자릿수를 계산한다.
    for i in range(len(word)):
        if word[i] in tmp:
            tmp[word[i]] += (10**(len(word)-i-1))
        else:
            tmp[word[i]] = (10**(len(word)-i-1))

tmp = sorted(tmp.items(), key = lambda x : x[1], reverse= True) # 자릿수값 기준으로 내림차순 정렬

num = 9
for i in range(len(tmp)): # 자릿수값이 큰 순서대로 숫자를 부여해준다.
    new[tmp[i][0]] = num
    num -= 1

result = 0
for word in words: # 알파벳을 숫자로 변환
    tmpresult = ""
    for w in word:
        tmpresult += str(new[w])
    result += int(tmpresult)
print(result)
