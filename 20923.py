from collections import deque
N,M = map(int,input().split())
do_queue  = deque()
su_queue = deque()

for _ in range(N):
    do,su = map(int,input().split())
    do_queue.append(do)
    su_queue.append(su)

do_check = 0
su_check = 0
do_tmp = []
su_tmp = []
for m in range(M):
    if m % 2 == 0:
        do_check = do_queue.pop()
        do_tmp.append(do_check)
    else:
        su_check = su_queue.pop()
        su_tmp.append(su_check)

    if len(do_queue) == 0:
        print("su")
        exit()
    elif len(su_queue) == 0:
        print("do")
        exit()

    if do_check + su_check == 5:
        for i in range(len(su_tmp)):
            su_queue.appendleft(su_tmp[i])
        for i in range(len(do_tmp)):
            su_queue.appendleft(do_tmp[i])

    elif (do_check == 5) or (su_check == 5):
        for i in range(len(do_tmp)):
            do_queue.appendleft(do_tmp[i])
        for i in range(len(su_tmp)):
            do_queue.appendleft(su_tmp[i])

if len(do_queue) > len(su_queue):
    print("do")
elif len(do_queue) < len(su_queue):
    print("su")
elif len(do_queue) == len(su_queue):
    print("dosu")