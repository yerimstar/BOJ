T = int(input())
for t in range(T):
    A, B = map(int, input().split())
    print("Case #%d: %d + %d = %d" %(t+1,A,B,A+B))