# 2 x n 타일링
n = int(input())

d = [0,1,2]
for i in range(3,n+1):
    d.append((d[i-1]+d[i-2]))

print(d[n] % 10007)