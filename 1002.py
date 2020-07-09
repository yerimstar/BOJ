import math
T = int(input())
for i in range(T):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())
    d = math.sqrt((x2-x1)**2+(y2-y1)**2)
    r_sum = r1+r2
    r_diff = abs(r1-r2)
    if (d == 0) & (r_diff == 0):
        print("-1")
    elif (r_diff < d) & (d < r_sum):
        print("2")
    elif (r_sum == d) | (r_diff == d):
        print("1")
    elif (r_sum < d) | (d < r_diff):
        print("0")
