def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
def lcm(a,b):
    c = gcd(a,b)
    return int(c*(a/c)*(b/c)) # return int(a*b/c)
A,B = map(int,input().split())
print(gcd(A,B))
print(lcm(A,B))
