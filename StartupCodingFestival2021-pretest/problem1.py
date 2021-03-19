# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
n,k = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
answer = 1
n -= k
answer += (n//(k-1))
if n%(k-1)!=0:
	answer+=1
print(answer)
