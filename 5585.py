money = 1000-int(input()) # 1000엔 - 지불할 돈
lst = [500,100,50,10,5,1]
cnt = 0 # 잔돈 개수

for l in lst:
    cnt += money // l
    money %= l

print(cnt)
