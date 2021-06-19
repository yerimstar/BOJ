N,K = map(int,input().split())
lst = []
cnt = 0

for i in range(N):
    lst.append(int(input()))

lst.sort(reverse=True)

for i in range(N):
    cnt += K // lst[i]
    K %= lst[i]

print(cnt)