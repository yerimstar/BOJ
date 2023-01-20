# 수 묶기
# 중요한 키포인트 지점 - 음수, 0, 1

N = int(input()) # 수열의 크기

# 수열 입력받기 (음수, 양수,0,1 분리)
negative = []
positive = []
zero = 0
one = 0
for _ in range(N):
    num = int(input())
    if num < 0: # 음수에 0 포함한 이유 - 음수 개수에 따라서 0을 없앨지 곱할지 판단하기 위함
        negative.append(num)
    elif num == 0:
        zero += 1
    elif num == 1:
        one += 1
    elif num > 1:
        positive.append(num)

# 음수 정렬 - 오름차순
negative = sorted(negative)
# 양수 정렬 - 내림차순
positive = sorted(positive,reverse=True)

result = 0

# 음수, 0 처리
negative_len = len(negative)
if negative_len % 2 == 0: # 음수 짝수개 -> 2개씩 묶기
    for i in range(0,negative_len,2):
        result += negative[i] * negative[i+1]
elif negative_len % 2 == 1: # 음수 홀수개 -> 2개씩 묶고 나머지는 0의 개수에 따라서 더할지 말지 결정하기
    for i in range(0,negative_len-1,2):
        result += negative[i] * negative[i+1]
    if zero == 0: # 0인 값이 없으면 음수랑 0을 곱할 수 없기 때문에 마지막 음수값을 더해줘야 한다
        result += negative[-1]

# 양수 처리
positive_len = len(positive)
if positive_len % 2 == 0:
    for i in range(0,positive_len,2):
        result += positive[i] * positive[i+1]
elif positive_len % 2 == 1:
    for i in range(0,positive_len-1,2):
        result += positive[i] * positive[i+1]
    result += positive[-1] # 마지막 값 더해주기

# 1 처리
if one > 0:
    result += one
print(result)
