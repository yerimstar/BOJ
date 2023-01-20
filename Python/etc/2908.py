num1, num2 = input().split()
new_num1 = int(''.join(reversed(num1)))
new_num2 = int(''.join(reversed(num2)))
if new_num1 > new_num2:
    print(new_num1)
else:
    print(new_num2)