T = int(input()) # T초 입력
A,B,C = 0,0,0
lst = [300,60,10] # 5분, 1분, 10초

A += T//lst[0]
T %= lst[0]
B += T//lst[1]
T %= lst[1]
C += T//lst[2]
T %= lst[2]

if T != 0:
    print("-1")
else:
    print(A,B,C)