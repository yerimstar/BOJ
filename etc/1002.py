# 두 원 사이의 관계
import math
T = int(input())
for i in range(T):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())
    d = math.sqrt((x2-x1)**2+(y2-y1)**2)  # 두 점 사이의 거리
    r_sum = r1+r2 # 반지름 합
    r_diff = abs(r1-r2) # 반지름 차
    if (d == 0) & (r_diff == 0): # 두 원이 일치하는 경우
        print("-1")
    elif (r_diff < d) & (d < r_sum): # 두 원이 두 점에서 만나는 경우
        print("2")
    elif (r_sum == d) | (r_diff == d): # 두 원이 한 점에서 만나는 경우 ( 내접, 외접 )
        print("1")
    elif (r_sum < d) | (d < r_diff): # 두 원이 만나지 않는 경우
        print("0")
