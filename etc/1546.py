num = int(input())
scores = list(map(int,input().split()))
max_score = max(scores)
new_score = []
for score in scores:
    new_score.append(round(score/max_score*100,2))
new_average = (sum(new_score)/num)
print(new_average)