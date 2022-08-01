word = input()
k = len(word)//10+1
for i in range(k):
    print(word[i*10:i*10+10])
