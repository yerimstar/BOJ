# 두 용액
import sys

N = sys.stdin.readline().strip() # 전체 용액의 수

solution = list(map(int,sys.stdin.readline().split())) # 용액

mixed_solution = list(set([(min(x,y),max(x,y),abs(x+y)) for x in solution for y in solution if x != y]))
mixed_solution.sort(key=lambda x : x[2])
print(mixed_solution[0][0],mixed_solution[0][1])

