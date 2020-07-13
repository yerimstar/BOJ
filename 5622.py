word = input()
dial = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
t = 0
for w in word: # 입력받은 단어를 하나씩 끊어서 한 문자씩 비교한다
    for d in dial: # dial을 돌면서 위에 해당하는 문자가 포함된 위치를 찾는다.
        if w in d:
            t += dial.index(d)+3 # ABC부터 3초씩 걸리므로 +3을 해서 시간을 구한다.
print(t)