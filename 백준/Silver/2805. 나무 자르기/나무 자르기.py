trees_num, target = map(int, input().split())
trees = list(map(int, input().split()))
high = max(trees)
low = 0
answer = 0
while low<=high:
    mid = (low+high)//2
    sum = 0
    for i in range(trees_num):
        if trees[i] - mid > 0:
            sum += (trees[i] - mid)
    if sum < target:
        high = mid-1
    else:
        low = mid+1
        answer = mid
print(answer)