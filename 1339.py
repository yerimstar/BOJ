N = int(input())
num = list(range(10))
alpha = []
tmp = {}

for _ in range(N):
    alpha.append(input())

alpha.sort(key = lambda x : len(x), reverse=True)

for i in range(N):
    for j in range(len(alpha[i])):
        val = alpha[i][j]
        if len(tmp) == 0:
            tmp[val] = str(max(num))
            num.remove(max(num))
        else:
            if val in tmp:
                continue
            else:
                tmp[val] = str(max(num))
                num.remove(max(num))
result = 0
for i in range(N):
    tmpresult = ""
    for j in range(len(alpha[i])):
        tmpresult += tmp[alpha[i][j]]
    result += int(tmpresult)
print(tmp)
print(result)