# 암기왕
# 교재 실전문제 - 부품찾기
import sys
def binary(array,target,start,end):
    while(start <= end):
        mid = (start+end)//2
        if array[mid] == target: # 값 발견시 mid 반환
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

def fnote():
    N = int(sys.stdin.readline())
    note1 = list(map(int,sys.stdin.readline().split()))
    note1.sort() # 이진 탐색을 위해 정렬
    M = int(sys.stdin.readline())
    note2 = list(map(int,sys.stdin.readline().split()))

    for num in note2:
        result = binary(note1,num,0,N-1)
        if result != None:
            print("1", end = '\n')
        else:
            print("0", end = '\n')

T = int(sys.stdin.readline())
for i in range(T):
    fnote()