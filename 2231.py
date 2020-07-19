N = int(input())
num = 0
for i in range(1,N+1):
    temp = [int(i) for i in str(i)]
    temp.append(i)
    if sum(temp) == N:
        num = temp[-1]
        break
print(num)
