N = int(input())
for i in range(1,2*N-1):
    if i % 2 == 1:
        print("* " * (i // 2) + "*" * (4 * N - 2 * i - 1) + " *" * (i // 2))
    else:
        print("* " * (i // 2) + " " * (4 * N - 2 * i - 3) + " *" * (i // 2))

for i in range(2*N-1,0,-1):
    if i % 2 == 1:
        print("* " * (i // 2) + "*" * (4 * N - 2 * i - 1) + " *" * (i // 2))
    else:
        print("* " * (i // 2) + " " * (4 * N - 2 * i - 3) + " *" * (i // 2))