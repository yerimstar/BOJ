L,P = map(int,input().split())
checks = list(map(int,input().split()))
size = L*P
for check in checks:
    print(check-size,end = ' ')
