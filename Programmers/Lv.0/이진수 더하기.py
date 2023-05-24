def bin_to_dec(s):
    dec = 0
    mul = 1
    while len(s) > 0:
        dec += (int(s[-1]) * mul)
        s = s[:-1]
        mul *= 2
    return dec
def dec_to_bin(n):
    if n == 0:
        return '0'
    bin = ''
    while n > 0:
        bin = str(n%2) + bin
        n //= 2
    return bin
def solution(bin1, bin2):
    answer = dec_to_bin(bin_to_dec(bin1) + bin_to_dec(bin2))
    return answer