number = []
remainders = []
check = []
for i in range(10):
    number.append(int(input()))
    remainders.append(number[i]%42)
for remainder in remainders:
    if remainder in check:
        pass
    else:
        check.append(remainder)
print(len(check))

"""
number = []
for i in range(10):
    num = int(input())
    number.append(num%42)
number = set(number)
print(len(number))
"""