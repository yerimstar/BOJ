N = int(input())
distance = list(map(int,input().split()))
money = list(map(int,input().split()))[:-1]
minPrice = money[0]
result = minPrice * distance[0]

for i in range(1,N-1):
    if money[i] < minPrice:
        minPrice = money[i]
    result += minPrice * distance[i]
print(result)


