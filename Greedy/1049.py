# 기타줄
N,M = map(int,input().split())
packagePrice = 1001
price = 1001
# 각 브랜드의 가격
for _ in range(M):
    a,b = map(int,input().split())
    packagePrice = min(packagePrice,a) # 최소 패키지 가격
    price = min(price,b) # 최소 낱개 가격

# 6으로 나누었을 때 나머지에 대한 가격 체크
# 패키지로 사는 것이 더 저렴한지, 낱개로 해당 개수만큼 사는 것이 저렴한지
check = min(packagePrice,price*(N % 6))
# 패키지(6개)에 대한 가격도 체크
print(min(packagePrice*(N//6),price*(N//6)*6)+check)

