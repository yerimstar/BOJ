N = int(input()) # N명
P = input()
lst = []
cnt = 0

for i in range(N):
    lst.append(int(P.split(" ")[i]))

lst.sort()

for i in range(N):
    tmp = lst[0:i+1]
    cnt += sum(tmp)

print(cnt)