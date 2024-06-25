n = int(input())
fruits = list(map(int, input().split()))
used = {}
left = 0
right = 0
result = 0
while left < n:
    while right < n:
        if fruits[right] not in used.keys():
            used[fruits[right]] = 0
        used[fruits[right]] += 1
        right += 1
        if len(used.keys()) > 2:
            right -= 1
            del used[fruits[right]]
            break
    result = max(result, right-left)
    used[fruits[left]]-=1
    if used[fruits[left]] == 0:
        del used[fruits[left]]
    left += 1
print(result)