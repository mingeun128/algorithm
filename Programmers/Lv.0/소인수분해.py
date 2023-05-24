# your code goes here
def get_prime_list(n):
    is_prime = [True] * (n+1)
    for i in range(2,n+1):
        if is_prime[i] == True:
            for j in range(i*2,n+1,i):
                is_prime[j] = False
    prime_list = [i for i in range(2,n+1) if is_prime[i] == True]
    return prime_list
def solution(n):
    answer = []
    prime_list = get_prime_list(n)
    print(prime_list)
    i = 0
    while i < n:
        if n % prime_list[i] == 0:
            n //= prime_list[i]
            if prime_list[i] not in answer:
                answer.append(prime_list[i])
        else:
            i+=1
    return answer