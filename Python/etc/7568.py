N = int(input())
people = []
for i in range(N):
    x,y = map(int,input().split())
    people.append((x,y))

for i in range(N):
    count = 1
    for j in range(N):
        if (people[i][0] < people[j][0] and people[i][1] < people[j][1]):
            count += 1
    print(count,end = ' ')
