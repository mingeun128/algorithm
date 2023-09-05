n = int(input())
count = 1
i = 6
st = 2
if n == 1:
    print(count)
else:
    while True:
        count += 1
        if st <= n and (st + i) > n:
            break
        else:
            st += i
            i += 6
    print(count)