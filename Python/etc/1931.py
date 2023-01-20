T = int(input()) # 회의의 수
start, end, cnt = 0,0,0
lst = []

for i in range(T): # T개의 회의를 입력받고 회의들을 lst에 저장한다.
    A, B = map(int,input().split())
    lst.append([A,B])

lst.sort(key=lambda x : (x[1],x[0])) # 끝나는 시간을 기준으로 오름차순함 정렬한 뒤, 시작하는 시간으로 오름차순 정렬

for i in range(T):
    if (end <= lst[i][0]):
        end = lst[i][1]
        cnt += 1
print(cnt)


