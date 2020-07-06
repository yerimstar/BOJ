a = []
a = input().split()
a = [int(i) for i in a]
b = sorted(a)
c = sorted(a,reverse=True)

if a == b:
    print("ascending")
elif a == c:
    print("descending")
else:
    print("mixed")