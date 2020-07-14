import sys
def check(x,y,i):
    if i in number[x]:
        return False
    for j in range(9):
        if number[j][y] == i:
            return False
    a = x//3*3
    b = y//3*3
    for k in range(3):
        for l in range(3):
            if number[a+k][b+l] == i:
                return False
    return True

def sudoku(count):
    if count == len(zero):# zero에 있는 값들이 모두 갱신되면 전체 스도쿠를 출력한다
        for i in number:
            for j in i:
                print(j,end = ' ')
            print()
        sys.exit()
    else:
        for i in range(1,10):
            x = zero[count][0]
            y = zero[count][1]
            if check(x,y,i):
                number[x][y] = i
                sudoku(count+1)
                number[x][y] = 0


number = [list(map(int, input().split())) for _ in range(9)] # 주어진 스도쿠 문제
zero = [(i, j) for i in range(9) for j in range(9) if number[i][j] == 0] # 비어있는 공간의 i,j값 저장
sudoku(0)