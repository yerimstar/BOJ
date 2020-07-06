word = input()
S = list(word)
alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for alphabet in alphabets:
    if alphabet in S:
        print(S.index(alphabet),end = ' ')
    else:
        print("-1",end = ' ')

"""
아스키코드 사용
word = input()
S = list(word)
alphabets = list(map(chr,range(97,123)))
for alphabet in alphabets:
    if alphabet in S:
        print(S.index(alphabet),end = ' ')
    else:
        print("-1",end = ' ')
"""