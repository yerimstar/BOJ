# 두 용액
import sys

N = sys.stdin.readline().strip() # 전체 용액의 수

solution = list(map(int,sys.stdin.readline().split())) # 용액

acid_solution = [x for x in solution if x > 0]
alkali_solution = [x for x in solution if x < 0]

if len(alkali_solution) == 0: # 산성 용액만 있는 경우 -> 양수
    acid_solution = sorted(acid_solution) # 산성 용액 오름차순 정렬
    print(acid_solution[0],acid_solution[1])
elif len(acid_solution) == 0: # 알칼리성 용액만 있는 경우 -> 음수
    alkali_solution = sorted(alkali_solution) # 알칼리 용액 오름차순 정렬
    print(alkali_solution[-2],alkali_solution[-1])
else: # 두 용액 모두 있는 경우
    mixed_solution = list(set([(min(x,y),max(x,y),abs(x+y)) for x in solution for y in solution if x != y]))
    mixed_solution.sort(key=lambda x : x[2])
    print(mixed_solution[0][0],mixed_solution[0][1])
