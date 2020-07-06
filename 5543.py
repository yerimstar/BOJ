import sys
hamburger = []
beverage = []
for i in range(3):
    input = int(sys.stdin.readline())
    hamburger.append(input)
for i in range(2):
    input = int(sys.stdin.readline())
    beverage.append(input)
print(min(hamburger)+min(beverage)-50)