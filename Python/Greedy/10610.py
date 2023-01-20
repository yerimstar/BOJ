# 30
n = input()
# 10의 배수 판별법 = 일의 자리 숫자가 0인 수
if "0" not in n:
    print(-1)
# 10의 배수 조건 성립, 3의 배수 조건 판별
else:
    # 각 자리 수의 합 구하기
    nSum = sum(map(int,n))

    # 3의 배수 판별법 = 각 자리 수의 합이 3의 배수
    if nSum % 3 == 0:
        # 가장 큰 수를 구해야 하기 때문에 내림차순 정렬
        n = sorted(n,reverse=True)
        print("".join(n))
    else:
        print(-1)