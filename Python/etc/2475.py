checks = list(map(int,input().split()))
num = [x**2 for x in checks]
print(sum(num)%10)