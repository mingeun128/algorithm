# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
def count_gift(n,m):
    if n < 5:
        return 0
    if n + m < 12:
        return 0
    change_count = 0
    if m >= 7:
	change_count = min(n//5, m//7)
	n-=(change_count*5)
	m-=(change_count*7)
	if n >= 5 and n+m >= 12:
	    n-=(12-m)
	    m=0
	    change_count= change_count + (n//12) + 1
	else:
            n-=(12-m)
            m=0
            change_count= change_count + (n//12) + 1
    return change_count

t = int(sys.stdin.readline())
for i in range(t):
    n,m = map(int,sys.stdin.readline().split())
    print(count_gift(n,m))
