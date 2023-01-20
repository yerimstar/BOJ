num = int(input())
for i in range(num):
    sum = 0
    score = 0
    tests = input()
    for test in tests:
        if test == 'O':
            score += 1
            sum += score
        elif test == 'X':
            score = 0
    print(sum)