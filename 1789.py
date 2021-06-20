S = int(input())
num = 1

while True:
    if S >= num:
        S = S-num
        num += 1
    else:
        break

print(num-1)