n, needs = map(int, input().split())
lans = []
for i in range(n):
    lans.append(int(input()))
min = 1
max = max(lans)
answer = 0
while(min <= max):
    mid = (max+min)//2
    m = 0
    for i in lans:
        m+=(i//mid)
    if m < needs:
        max = mid - 1
    if m >= needs:
        if answer < mid:
            answer = mid
        min = mid + 1
print(answer)