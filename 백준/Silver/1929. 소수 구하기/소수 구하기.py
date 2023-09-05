MAX_NUM = 1000001
prime_check = [True] * MAX_NUM
prime_check[0] = False
prime_check[1] = False
n,m = map(int, input().split())
for i in range(2,MAX_NUM):
    for j in range(i*2,MAX_NUM,i):
        prime_check[j] = False
for i in range(n,m+1):
    if prime_check[i] == True:
        print(i)