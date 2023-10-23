import sys
price = int(sys.stdin.readline().rstrip())
product_cnt = int(sys.stdin.readline().rstrip())
total_price = 0
for _ in range(product_cnt):
    p,c = map(int, sys.stdin.readline().rstrip().split())
    total_price += (p*c)
if total_price == price:
    print('Yes')
else:
    print('No')