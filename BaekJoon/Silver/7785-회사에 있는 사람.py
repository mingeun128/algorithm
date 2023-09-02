import sys
n = int(sys.stdin.readline())
employee = {}
for i in range(n):
    log = tuple(sys.stdin.readline().split())
    if log[1] == 'enter':
        employee[log[0]] = log[1]
    elif log[1] == 'leave':
        del employee[log[0]]
answers = list(employee.keys())
answers.sort(reverse=True)
for i in answers:
    print(i)