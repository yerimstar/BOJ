def seven(count):
    if count == len(dasom):
        print()
    else:
        for i in range(4):

girls = [list(input()) for _ in range(5)]
dasom = [(i,j) for i in range(5) for j in range(5) if girls[i][j] == 'S']
print(dasom)