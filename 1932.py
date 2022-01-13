# 정수 삼각형
import sys

n = int(sys.stdin.readline())
triangle = []
for i in range(n):
    triangle.append(list(map(int,sys.stdin.readline().split())))
print(triangle)

d = [0] * n

result = triangle[0][0] # 시작 값
check_index = 0 # 왼쪽, 오른쪽 값 판단 기준
for i in range(1,n):

