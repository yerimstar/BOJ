"""
런타임 에러
import sys
data = []
for i in range(3):
    data.append(list(map(int,sys.stdin.readline().split())))
for i in range(3):
    if i < 2:
        if data[i][0] == data[i+1][0]:
            x1 = data[i][0]
    if i == 2:
        if data[2][0] == data[0][0]:
            x1 = data[0][0]
for i in range(3):
    if data[i][0] != x1:
        x2 = data[i][0]
        y1 = data[i][1]
    for i in range(3):
        if y1 != data[i][1]:
             y2 = data[i][1]
print(x2,y2)
"""
import sys
x_list = []
y_list = []
for i in range(3):
    x,y = (map(int,sys.stdin.readline().split()))
    x_list.append(x)
    y_list.append(y)
for i in range(3):
    if x_list.count(x_list[i]) == 1:
        x = x_list[i]
    if y_list.count(y_list[i]) == 1:
        y = y_list[i]
print(x,y)