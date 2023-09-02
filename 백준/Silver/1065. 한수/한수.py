n = int(input())
ans = 99
    
if n < 100:
    ans = n
else:
    if n == 1000:
        n -= 1
            
    for i in range(101, n+1):
        if ((i//100) + (i%10)) == 2*((i%100)//10):
            ans += 1
            
print(ans)