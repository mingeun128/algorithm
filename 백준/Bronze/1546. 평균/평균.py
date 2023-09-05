n = int(input())
score = list(map(int,input().split()))
max_score = max(score)
summ = 0
for i in score:
    summ += (i/max_score*100)
avg = summ / n
print(avg)