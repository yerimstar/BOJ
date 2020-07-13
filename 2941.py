check = ['c=','c-','dz=','d-','lj','nj','s=','z=']
word = input()
for c in check:
    word = word.replace(c,'#')
print(len(word))
