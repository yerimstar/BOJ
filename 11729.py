#하노이 탑 - 재귀
import sys
def hanoi(N,start,temp,end):
    if N == 1:
        print(start,end) # 이동 완료
    else:
        hanoi(N-1,start,end,temp) # n-1개를 보조 기둥으로 이동
        hanoi(1,start,temp,end) # 가장 큰 원반을 최종 기둥으로 이동
        hanoi(N-1,temp,start,end) # 보조 기둥에 있는 n-1개의 원반들을 최종 기둥으로 이동
N = int(sys.stdin.readline()) # 원판의 개수
print(2**N-1) # 옮긴 횟수 - 등비수열의 합 (점화식 = P(1) = 1, P(n) = 2P(n-1)+1)
hanoi(N,1,2,3) # 1 - 시작 기둥, 2 - 보조 기둥, 3 - 최종 기둥
