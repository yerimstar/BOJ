# 문서검색
document = input()
word = input()
cnt = 0
while True:
    # 찾으려는 단어가 존재한다면
    try:
        # 단어 찾기
        document = document[document.index(word) + len(word):]
        cnt += 1
        # 현재 문서의 길이가 단어의 길이보다 짧다면 종료
        if len(document) < len(word):
            break
    except ValueError:
        break
print(cnt)