word = input()
dial = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
t = 0
for w in word:
    for d in dial:
        if w in d:
            t += dial.index(d)+3
print(t)