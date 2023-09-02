# your code goes here
import sys
def checkNum(n):
    i=1
    sum=0
    while(True):
        sum = i * (i+1) //2
        if n <= sum:
            break
        i+=1
    return i
a,b = map(int, sys.stdin.readline().split())
startNum = checkNum(a)
lastNum = checkNum(b)

if startNum == lastNum:
	answer = startNum * (b-a+1)
else:
	startNumLastIndex = startNum * (startNum + 1) //2
	lastNumBeforeIndex = lastNum * (lastNum - 1) // 2
	answer = startNum * (startNumLastIndex - a + 1)
	answer = answer + (lastNum * (b - lastNumBeforeIndex))
	for i in range(startNum+1, lastNum):
	    answer += (i*i)
print(answer)