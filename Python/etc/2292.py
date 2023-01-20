N = int(input())
count = 1
range = 1
temp = 1
while(1):
    if range >= N:
        break
    temp = 6*count
    count += 1
    range += temp
print(count)