N = int(input())
distance = list(map(int,input().split()))
money = list(map(int,input().split()))[:-1]

result = 0
endIndex = len(distance)

while True:
    minMoney = min(money)
    startIndex = money.index(minMoney)

    for i in range(startIndex, endIndex):
        result += (minMoney * distance[i])

    if startIndex == 0:
        break
    else:
        if startIndex > 1:
            money = money[:startIndex]
            endIndex = startIndex
        else:
            result += money[0] * distance[0]
            break

print(result)